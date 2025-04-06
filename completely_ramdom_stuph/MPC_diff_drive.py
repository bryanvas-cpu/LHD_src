import casadi as ca
import numpy as np
import matplotlib.pyplot as plt

def generate_zigzag_trajectory(t_array, x_speed=0.6, y_amplitude=0.5, period=4.0):
	x = x_speed * t_array
	phase = (t_array % period) / period
	y = 4 * y_amplitude * np.abs(phase - 0.5) - y_amplitude
	return x, y

# Parameters
dt = 0.1
N = 20
T = 100
nx = 3
nu = 2

# Cost weights
Q = np.diag([10.0, 10.0, 0.05])
R = np.diag([0.01, 0.01])

# Constraints
v_max = 1.2
v_min = -1.2
omega_max = np.pi / 4
omega_min = -np.pi / 4

# Dynamics
x = ca.SX.sym('x')
y = ca.SX.sym('y')
theta = ca.SX.sym('theta')
v = ca.SX.sym('v')
omega = ca.SX.sym('omega')
state = ca.vertcat(x, y, theta)
control = ca.vertcat(v, omega)
rhs = ca.vertcat(v * ca.cos(theta),
				 v * ca.sin(theta),
				 omega)
f = ca.Function('f', [state, control], [rhs])

# Create time array and trajectory
total_time = (T + N) * dt
t_array = np.arange(0, total_time, dt)
x_ref_full, y_ref_full = generate_zigzag_trajectory(t_array)
dx = np.gradient(x_ref_full)
dy = np.gradient(y_ref_full)
theta_ref_full = np.arctan2(dy, dx)

last_x = x_ref_full[-1]
last_y = y_ref_full[-1]
last_theta = theta_ref_full[-1]

x_ref_full = np.concatenate([x_ref_full, np.full(N, last_x)])
y_ref_full = np.concatenate([y_ref_full, np.full(N, last_y)])
theta_ref_full = np.concatenate([theta_ref_full, np.full(N, last_theta)])

# x_ref_full = np.concatenate([x_ref_full, np.full(N + 1, x_ref_full[-1])])
# y_ref_full = np.concatenate([y_ref_full, np.full(N + 1, y_ref_full[-1])])
# theta_ref_full = np.concatenate([theta_ref_full, np.full(N + 1, theta_ref_full[-1])])

def solve_mpc_step(x0, x_ref_traj, y_ref_traj, theta_ref_traj):
	X = ca.SX.sym('X', nx, N + 1)
	U = ca.SX.sym('U', nu, N)
	cost = 0
	g = []

	g += [X[:, 0] - x0]

	for k in range(N):
		x_ref_k = x_ref_traj[k]
		y_ref_k = y_ref_traj[k]
		theta_ref_k = theta_ref_traj[k]
		x_ref_vec = ca.vertcat(x_ref_k, y_ref_k, theta_ref_k)

		e = X[:, k] - x_ref_vec
		u = U[:, k]
		cost += ca.mtimes([e.T, Q, e]) + ca.mtimes([u.T, R, u])

		x_next = X[:, k] + dt * f(X[:, k], U[:, k])
		g += [X[:, k + 1] - x_next]

	opt_vars = ca.vertcat(ca.reshape(X, -1, 1), ca.reshape(U, -1, 1))
	nlp = {'x': opt_vars, 'f': cost, 'g': ca.vertcat(*g)}
	opts = {'ipopt.print_level': 0, 'print_time': 0}
	solver = ca.nlpsol('solver', 'ipopt', nlp, opts)

	x_guess = np.tile(x0.reshape(-1, 1), (1, N + 1))
	u_guess = np.zeros((nu, N))
	lbx = [-ca.inf] * (nx * (N + 1)) + [v_min, omega_min] * N
	ubx = [ca.inf] * (nx * (N + 1)) + [v_max, omega_max] * N
	lbg = [0.0] * ((N + 1) * nx)
	ubg = [0.0] * ((N + 1) * nx)

	args = {
		'x0': np.concatenate([x_guess.flatten(), u_guess.flatten()]),
		'lbx': lbx,
		'ubx': ubx,
		'lbg': lbg,
		'ubg': ubg
	}

	sol = solver(**args)
	sol_xu = sol['x'].full().flatten()
	u0 = sol_xu[(N + 1) * nx:(N + 1) * nx + nu]
	return u0

# Simulation
x0 = np.array([0.0, -1.0, 0.0])
x_hist = [x0.copy()]
u_hist = []

t0 = 0
while True:
    # Slice out remaining trajectory
    x_ref_traj = x_ref_full[t0:t0 + N + 1]
    y_ref_traj = y_ref_full[t0:t0 + N + 1]
    theta_ref_traj = theta_ref_full[t0:t0 + N + 1]

    # If there aren't enough points left, break the loop
    if len(x_ref_traj) < N + 1:
        print(f"Terminating at t0 = {t0} due to insufficient reference points.")
        break

    # Solve one MPC step
    u0 = solve_mpc_step(x0, x_ref_traj, y_ref_traj, theta_ref_traj)

    # Apply control and simulate system forward
    dx = f(x0, u0).full().flatten()
    x0 = x0 + dt * dx

    # Log
    x_hist.append(x0.copy())
    u_hist.append(u0.copy())
    print(f"Step {t0}: Control = {u0}")

    # Advance time
    t0 += 1

x_hist = np.array(x_hist)

# Plot
# Setup live plot
plt.ion()
fig, ax = plt.subplots(figsize=(8, 8))
ref_plot, = ax.plot(x_ref_full, y_ref_full, 'r--', label='Reference Path')
robot_path, = ax.plot([], [], 'b-', label='Robot Path')
robot_dot, = ax.plot([], [], 'bo', label='Robot', markersize=8)
target_dot, = ax.plot([], [], 'ro', label='Target', markersize=8)

ax.set_aspect('equal')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Live NMPC Trajectory Tracking")
ax.grid(True)
ax.legend()

# Initial state and logs
x0 = np.array([0.0, -1.0, 0.0])
x_hist = [x0.copy()]
u_hist = []

t0 = 0
while True:
    # Extract reference segment
    x_ref_traj = x_ref_full[t0:t0 + N + 1]
    y_ref_traj = y_ref_full[t0:t0 + N + 1]
    theta_ref_traj = theta_ref_full[t0:t0 + N + 1]

    # Stop if there aren't enough waypoints left
    if len(x_ref_traj) < N + 1:
        print(f"Terminating at t0 = {t0} due to insufficient reference points.")
        break

    # Solve MPC for current timestep
    u0 = solve_mpc_step(x0, x_ref_traj, y_ref_traj, theta_ref_traj)
    dx = f(x0, u0).full().flatten()
    x0 = x0 + dt * dx

    # Logging
    x_hist.append(x0.copy())
    u_hist.append(u0.copy())

    # Live update
    xs = np.array(x_hist)
    robot_path.set_data(xs[:, 0], xs[:, 1])
    robot_dot.set_data(x0[0], x0[1])
    target_dot.set_data(x_ref_traj[0], y_ref_traj[0])
    plt.pause(0.01)

    t0 += 1  # Advance to next timestep

plt.ioff()
plt.show()
