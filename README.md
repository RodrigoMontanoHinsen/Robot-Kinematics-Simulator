🦾**Robot Kinematics Simulator (2-DOF)**

Python-based tool to calculate the end-effector position of a two-bar linkage robotic arm.

🎯**Overview**

This project solves the Forward Kinematics problem for a planar robotic arm. Given the lengths of the links and the joints angles, the program determines the exact (X, Y) coordinates of the robot's hand.

📐**Mathematical Logic**

The simulation uses Forward Kinematics Equations. For a 2-DOF arm, the position is determined by:

```math
X = L_1 \cos(\theta1) + L_2 \cos(\theta_1 + \theta_2)
```
Note: The code includes a built-in conversion from radians to degrees to ensure user-friendly inputs.

💻**Logic Flow**

graph LR

```mermaid

A[Link Lengths L1, L2] --> C{Logic Engine}
B[Joint Angles 01, 02] --> C
C --> D[Final X, Y Coordinates]
```

🚀**How to run**

Ensure you have Python installed.

Run python kinematics.py.

Input the link distances and angles when prompted.
