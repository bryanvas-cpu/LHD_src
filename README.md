# 🧭 Differential Drive Robot Navigation  
## Path Smoothing, Obstacle Avoidance & Nonlinear MPC Trajectory Tracking

This project implements a **complete navigation pipeline** for a differential drive robot, starting from discrete 2D waypoints and ending with smooth, dynamically feasible motion in the presence of obstacles.

The system integrates **path planning, spline-based smoothing, costmap-driven obstacle avoidance, and nonlinear model predictive control (NMPC)** to achieve accurate and robust trajectory tracking.

---

## 🚀 System Overview

The navigation stack is composed of three tightly coupled layers:

1. **Path Planning with Obstacle Awareness**
2. **Path Smoothing for Motion Feasibility**
3. **Trajectory Tracking using Nonlinear MPC**

Each layer is designed to preserve modularity while contributing to globally smooth and stable robot behavior.

---

## 🧩 Path Planning & Obstacle Avoidance

**File:**  
`lhd_automation/lhd_automation/path_planning_service.py`

### Key Features
- Uses **A\*** search on an **8-bit costmap**
- Obstacles and walls are assigned **increasing cost gradients**
- Regions closer to obstacles incur higher traversal cost

### Rationale
Instead of producing shortest-but-jagged paths, the costmap bias encourages trajectories that:
- Maintain safe clearance from obstacles  
- Avoid sharp turns near walls  
- Offer smoother downstream control behavior  

This approach balances **path optimality and motion flexibility**, making it suitable for real robotic systems.

---

## ✨ Path Smoothing

After planning, the discrete waypoint path is refined using **spline-based smoothing**.

### Description
Fits a smooth spline curve through a given (y, x) path and resamples it into a fixed number of evenly spaced points.  
This removes sharp turns and produces a continuous, smooth trajectory suitable for motion planning and visualization.

### Outcome
A **continuous, differentiable trajectory** that is well-suited for:
- Predictive control
- Velocity continuity
- Stable tracking performance

---

## 🎯 Trajectory Tracking — Nonlinear MPC

**File:**  
`lhd_automation/lhd_automation/MPC_diff_drive_class.py`

### Controller Details
- **Controller Type:** Nonlinear Model Predictive Control (NMPC)
- **States:** (x, y, θ)
- **Controls:** (v, ω)
- **Solver:** CasADi + IPOPT
- **Model:** Differential drive kinematics

### Objective
The NMPC minimizes:
- Tracking error with respect to the reference trajectory
- Control effort for smooth motion

While enforcing:
- System kinematics
- Velocity and angular rate constraints

At each iteration, the controller computes an optimal control sequence and applies only the **first control input**, enabling real-time operation.

---

## 🔁 Shifting (Receding) Horizon Control

A **shifting horizon strategy** is employed:

- The robot’s current state is updated at every control cycle
- The reference trajectory is shifted forward
- The NMPC problem is re-solved online

This provides:
- Continuous feedback correction
- Robustness to disturbances
- Predictive and adaptive control behavior

---

## 🛞 Vehicle Control Model

The vehicle uses **Articulated + Differential Steering**.

To achieve accurate locomotion control and odometry:
- Classical **differential drive kinematics** are fused with
- **Derived articulated joint kinematics**

This hybrid formulation improves:
- Turning accuracy
- Motion smoothness
- Odometry consistency in real-world operation

---

## 🎥 System Demonstration

Click below to visualize the complete navigation pipeline:

[![System Demonstration](https://img.youtube.com/vi/Xlj6dwbFPWI/maxresdefault.jpg)](https://youtu.be/Xlj6dwbFPWI)

---

## 📌 Summary

This project demonstrates a **full-stack robotic navigation system** featuring:
- Costmap-aware A\* path planning
- Spline-based path smoothing
- Nonlinear MPC with shifting horizon control
- Hybrid articulated + differential drive motion modeling

The resulting system produces **smooth, safe, and dynamically feasible motion**, designed with real robotic deployment in mind.
