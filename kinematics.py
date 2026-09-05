import math

def calculate_direct_kinematics(L1, L2, theta1_degrees, theta2_degrees):
    """
    Calculates the position (X, Y) of the wrist of a two-bar linkage robotic arm, given the degrees of their joints
    """
    #1. Convert degrees to radians
    theta1 = math.radians(theta1_degrees)
    theta2 = math.radians(theta2_degrees)
    
    #2. Direct Kinematics Equations
    x = L1 * math.cos(theta1) + L2 * math.cos(theta1 + theta2)
    y = L1 * math.sin(theta1) + L2 * math.sin(theta1 + theta2)
    
    return x, y

if __name__ == "__main__":
    L1 = 5.0        # distance shoulder -> elbow
    L2 = 3.0        # longitud elbow  -> wrist
    theta1 = 30     # degree of shoulder
    theta2 = 45     # degree of elbow
    
    x, y = calculate_direct_kinematics(L1, L2, theta1, theta2)
    
    print(f"With theta1={theta1}° and theta2={theta2}°:")
    print(f"The hand of the robot is in the position (X={x:.2f}, Y={y:.2f})")
    
