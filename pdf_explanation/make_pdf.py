from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import textwrap

def write_pdf(text, path, font_size=11):
    """Write multi-page PDF with automatic text wrapping and pagination."""
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    margin = 20 * mm
    line_height = font_size * 1.4

    # Start text object
    textobject = c.beginText(margin, height - margin)
    textobject.setFont("Helvetica", font_size)

    for line in text.splitlines():
        if line.strip() == "":
            textobject.textLine("")
        else:
            for wrapped in textwrap.wrap(line, 90):  # wrap long lines
                # Check if there's still space on page
                if textobject.getY() <= margin:
                    c.drawText(textobject)
                    c.showPage()
                    textobject = c.beginText(margin, height - margin)
                    textobject.setFont("Helvetica", font_size)
                textobject.textLine(wrapped)

    # Draw remaining text
    c.drawText(textobject)
    c.showPage()
    c.save()


# === Document 1: General Automation ===
doc_text = """
Automation of Robot Navigation with ROS and MPC
================================================

Overview
--------
This project implements an automated navigation pipeline for a differential-drive
robot using ROS (Robot Operating System) and Model Predictive Control (MPC).
The system allows a user to select a target site on a map. The automation then
computes and executes a safe and efficient path to the target.

Key Components
--------------
1. **User Interface**
   - The user selects a target location on a digital map (e.g., via a GUI or web-based interface).
   - The target coordinates are sent to the automation system.

2. **Path Planning Service**
   - Computes a feasible path from the robot's current location to the target site.
   - May use algorithms like graph search or geometric planners.
   - Outputs a reference trajectory that respects obstacles and environment layout.

3. **Model Predictive Control (MPC)**
   - Uses a dynamic model of the robot to optimize control inputs (wheel velocities).
   - Considers prediction horizon, system constraints, and path-following objectives.
   - Continuously updates control commands based on real-time feedback.

4. **ROS Client and Server Nodes**
   - **Server (`lhd_server.py`)**: Provides services to compute paths and control commands.
   - **Client (`lhd_client.py`)**: Interfaces with user input and sends goals to the server.
   - Communication is handled using ROS topics and services.

5. **Execution Layer**
   - The computed control signals are sent to the robot actuators (or a simulator).
   - The robot moves along the path while the system monitors progress.

Automation Flow
---------------
1. User selects a target site on the map.
2. Target coordinates are sent to the path planning service.
3. Path planner computes a trajectory and passes it to the MPC controller.
4. MPC computes optimal control commands considering robot dynamics and constraints.
5. ROS nodes publish commands to the robot.
6. Robot navigates autonomously to the target while the system continuously monitors and corrects.

Benefits of This Automation
----------------------------
- Human operator only needs to specify the goal, not the detailed motion.
- Optimized trajectories increase safety and efficiency.
- ROS modularity enables integration with sensors, simulators, or real robots.

Conclusion
----------
This automation framework demonstrates how modern robotics integrates user interfaces,
planning algorithms, and optimal control. By allowing goal selection on a map and
delegating the navigation to an MPC-driven ROS system, the robot can navigate efficiently
with minimal human intervention.
"""

write_pdf(doc_text, "general_automation_doc_fixed.pdf")


# === Document 2: NMPC with CasADi ===
doc_text_nmpc = """
Nonlinear Model Predictive Control (NMPC) with CasADi
======================================================

Overview
--------
This document explains the implementation of a Nonlinear Model Predictive Control (NMPC)
scheme for a differential-drive robot, based on the provided Python code that uses CasADi.

Key Concepts
------------
1. **Differential Drive Robot Model**
   - State: [x, y, theta]
   - Control: [v, omega]
   - Kinematics:
        x_dot = v * cos(theta)
        y_dot = v * sin(theta)
        theta_dot = omega

2. **Prediction Horizon**
   - The controller predicts the robot’s motion over N = 20 future timesteps.
   - Each timestep is of duration dt = 0.1 s.

3. **Cost Function**
   - Penalizes deviation from reference trajectory (Q matrix).
   - Penalizes control effort (R matrix).
   - Q = diag([1.0, 1.0, 0.05])
   - R = diag([0.08, 0.09])

4. **Constraints**
   - Velocity bounds: v ∈ [-0.2, 0.2] m/s
   - Angular velocity bounds: ω ∈ [-π/4, π/4] rad/s
   - Dynamics constraints ensure that predicted states follow robot motion equations.

5. **Optimization Problem**
   - Variables: Future states X (3x(N+1)) and controls U (2xN).
   - Objective: Minimize cost subject to constraints.
   - Solver: IPOPT (via CasADi nlpsol).

Implementation Details
----------------------
- `DiffDriveNMPC.__init__`: Initializes parameters, cost weights, and bounds.
- `_define_dynamics`: Defines robot kinematics in CasADi symbolic form.
- `_setup_solver`: Builds the nonlinear optimization problem with constraints and cost.
- `solve`: 
   1. Pads reference trajectory to horizon length.
   2. Creates optimization variables (X, U).
   3. Solves NLP with IPOPT.
   4. Extracts the first control input [v, ω].

Automation Workflow
-------------------
1. Current robot state x0 = [x, y, theta] is given.
2. Desired trajectory (x_ref, y_ref, theta_ref) is provided.
3. NMPC builds a prediction and optimizes controls.
4. Solver returns optimal v and ω for the current step.
5. Apply control → repeat at next timestep.

Benefits of NMPC
----------------
- Handles nonlinear robot dynamics.
- Optimizes performance while respecting constraints.
- Flexible: easy to adjust horizon length, cost weights, and constraints.

Conclusion
----------
The code demonstrates a compact and practical NMPC setup for differential-drive robots.
CasADi enables efficient symbolic modeling and nonlinear optimization, making this approach
suitable for real-time autonomous navigation tasks.
"""

write_pdf(doc_text_nmpc, "nmpc_explanation_fixed.pdf")
