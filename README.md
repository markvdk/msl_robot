# MSL Robot Workspace

This repository contains the ROS 2 Humble workspace for the MSL Robot project.

## Installation

### 1. Install ROS 2 Humble
Follow the official ROS 2 installation guide:  
[ROS 2 Humble Installation](https://docs.ros.org/en/humble/index.html)

After installation, add this to your `~/.bashrc` file:
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 2. Install Required Packages
Run the following commands to install dependencies:
```bash
sudo apt update
sudo apt install ros-humble-joint-state-publisher-gui ros-humble-xacro ros-humble-ros2-gz \
ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-ign-ros2-control \
ros-humble-moveit ros-humble-urdf-tutorial ros-humble-tf-transformations \
libserial-dev python3-pip python3-serial
```
```bash
sudo apt install ros-humble-rclcpp ros-humble-rclpy ros-humble-geometry-msgs \
ros-humble-std-msgs ros-humble-sensor-msgs ros-humble-nav-msgs ros-humble-tf2-ros \
ros-humble-tf2 libeigen3-dev ros-humble-ros2launch ros-humble-robot-state-publisher \
ros-humble-joy ros-humble-joy-teleop ros-humble-ament-lint-auto ros-humble-ament-lint-common
```

Optional for testing:
```bash
sudo apt install ros-humble-ament-lint-auto ros-humble-ament-lint-common
```

### 3. Setup Colcon and ROS Dependency Management
```bash
echo "source /usr/share/colcon_argcomplete/hook/colcon_argcomplete.bash" >> ~/.bashrc
source ~/.bashrc
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```
### 4. Install VSCode (Optional)
Install Visual Studio Code.

Recommended VSCode Extensions:
-   C/C++ (Microsoft)
-   C/C++ Extension Packages (Microsoft)
-   Python (Microsoft)
-   CMake (twxs)
-   CMaker Tools (Microsoft)
-   ROS (Microsoft)
-   XML (Red Hat)
-   XML Tools (Josh Johnson)

### Building the Project
Navigate to the workspace folder msl_robot_ws and run:
```bash
source install/setup.bash
colcon build --symlink-install
```

### Running the Project
Navigate to the workspace folder msl_robot_ws and run:
```bash
ros2 launch msl_robot_description msl_robot.launch.py
```
