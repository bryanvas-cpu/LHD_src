import casadi as ca
import numpy as np

class DiffDriveNMPC:
    def __init__(self, dt=0.1, N=20):
        self.dt = dt
        self.N = N
        self.nx = 3
        self.nu = 2

        self.Q = np.diag([1.0, 1.0, 0.05])
        self.R = np.diag([0.1, 0.2])

        self.v_max = 0.5
        self.v_min = -0.5
        self.omega_max = np.pi / 4
        self.omega_min = -np.pi / 4

        self._define_dynamics()
        self._setup_solver()

    def _define_dynamics(self):
        x = ca.SX.sym('x')
        y = ca.SX.sym('y')
        theta = ca.SX.sym('theta')
        v = ca.SX.sym('v')
        omega = ca.SX.sym('omega')
        state = ca.vertcat(x, y, theta)
        control = ca.vertcat(v, omega)

        rhs = ca.vertcat(
            v * ca.cos(theta),
            v * ca.sin(theta),
            omega
        )

        self.f = ca.Function('f', [state, control], [rhs])

    def _setup_solver(self):
        X = ca.SX.sym('X', self.nx, self.N + 1)
        U = ca.SX.sym('U', self.nu, self.N)

        P = ca.SX.sym('P', (self.N + 1) * self.nx)  # flattened ref trajectory
        X0 = ca.SX.sym('X0', self.nx)              # current state

        cost = 0
        g = [X[:, 0] - X0]  # initial state constraint

        for k in range(self.N):
            x_ref_k = P[k * self.nx:(k + 1) * self.nx]
            e = X[:, k] - x_ref_k
            u = U[:, k]
            cost += ca.mtimes([e.T, self.Q, e]) + ca.mtimes([u.T, self.R, u])
            x_next = X[:, k] + self.dt * self.f(X[:, k], U[:, k])
            g += [X[:, k + 1] - x_next]

        opt_vars = ca.vertcat(
            ca.reshape(X, -1, 1),
            ca.reshape(U, -1, 1)
        )

        nlp = {
            'x': opt_vars,
            'f': cost,
            'g': ca.vertcat(*g),
            'p': ca.vertcat(X0, P)
        }

        opts = {'ipopt.print_level': 0, 'print_time': 0}
        self.solver = ca.nlpsol('solver', 'ipopt', nlp, opts)

        # Variable bounds
        self.lbx = []
        self.ubx = []

        for _ in range(self.N + 1):
            self.lbx += [-ca.inf] * self.nx
            self.ubx += [ca.inf] * self.nx

        for _ in range(self.N):
            self.lbx += [self.v_min, self.omega_min]
            self.ubx += [self.v_max, self.omega_max]

    def solve(self, x0, x_ref, y_ref, theta_ref):
        if len(x_ref) < self.N + 1:
            # Pad with last point
            pad = self.N + 1 - len(x_ref)
            x_ref = np.pad(x_ref, (0, pad), 'edge')
            y_ref = np.pad(y_ref, (0, pad), 'edge')
            theta_ref = np.pad(theta_ref, (0, pad), 'edge')

        ref_traj = np.vstack([x_ref, y_ref, theta_ref]).T.flatten()
        params = np.concatenate([x0, ref_traj])

        x_guess = np.tile(x0.reshape(-1, 1), (1, self.N + 1))
        u_guess = np.zeros((self.nu, self.N))

        args = {
            'x0': np.concatenate([x_guess.flatten(), u_guess.flatten()]),
            'lbx': self.lbx,
            'ubx': self.ubx,
            'lbg': [0.0] * ((self.N + 1) * self.nx),
            'ubg': [0.0] * ((self.N + 1) * self.nx),
            'p': params
        }

        sol = self.solver(**args)
        sol_xu = sol['x'].full().flatten()
        u0 = sol_xu[(self.N + 1) * self.nx:(self.N + 1) * self.nx + self.nu]

        return u0.tolist()
