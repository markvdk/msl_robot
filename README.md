# MSL Robot

This repository contains the ROS 2 Humble workspace for the MSL Robot project.

## Installation
### 1. Clone the Repository
First, clone the repository to your local machine using Git. This will create a folder containing all the files in the repository:
```bash
cd ~ 
git clone https://github.com/markvdk/msl_robot.git
```
Navigate into the msl_robot_ws workspace directory to start the installation process
```bash
cd ~/msl_robot/msl_robot_ws
```
### 2. Install ROS 2 Humble on Ubuntu Linux 22.04

Follow the official ROS 2 installation guide:  
[ROS 2 Humble Installation](https://docs.ros.org/en/humble/index.html)

For your laptop or desktop choose the 'Desktop Install' version. But for the installation on the Raspberry Pi choose the 'ROS-Base Install (Bare Bones)' version. 

After installation, add this to your `~/.bashrc` file:
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 3. Setup ROS Dependency Management
```bash
sudo apt install python3-rosdep -y
```
Initialize rosdep (dependency manager for ROS 2)
```bash
sudo rosdep init
```
(FYI: The command sudo rosdep init should only be run once per system.)

```bash
rosdep update
```
Make sure you are in the workspace direcory and install rosdep in it. 
```bash
cd ~/msl_robot/msl_robot_ws
```
```bash
rosdep install --from-paths src --ignore-src -r -y
```

### 4. Install Required Packages
Run the following commands to install dependencies:
```bash
sudo apt update
sudo apt upgrade
```
For the Desktop Version (Recommended for full development with GUI tools)
```bash
sudo apt install ros-humble-joint-state-publisher-gui ros-humble-xacro ros-humble-ros-gz \
ros-humble-ros2-control ros-humble-ros2-controllers ros-humble-ign-ros2-control \
ros-humble-moveit ros-humble-urdf-tutorial ros-humble-tf-transformations \
ros-humble-rclcpp ros-humble-rclpy ros-humble-geometry-msgs \
ros-humble-std-msgs ros-humble-sensor-msgs ros-humble-nav-msgs ros-humble-tf2-ros \
ros-humble-tf2 libeigen3-dev ros-humble-ros2launch ros-humble-robot-state-publisher \
ros-humble-joy ros-humble-joy-teleop ros-humble-ament-lint-auto ros-humble-ament-lint-common \
libserial-dev python3-pip python3-serial python3-colcon-common-extensions
```
For the Barebones Version (Optimized for headless Raspberry Pi setup)
```bash
sudo apt install ros-humble-ros-base ros-humble-xacro ros-humble-ros2-control \
libserial-dev python3-pip python3-serial python3-colcon-common-extensions \
ros-humble-rclcpp ros-humble-rclpy ros-humble-geometry-msgs ros-humble-ros2-controllers \
ros-humble-std-msgs ros-humble-sensor-msgs ros-humble-nav-msgs ros-humble-tf2-ros \
ros-humble-tf2 libeigen3-dev ros-humble-ros2launch ros-humble-robot-state-publisher
```

Optional for testing:
```bash
sudo apt install ros-humble-ament-lint-auto ros-humble-ament-lint-common
```

### 5. Setup Colcon
```bash
echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
source ~/.bashrc
```


### 5. Install VSCode (Optional)
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
Make sure you are in the workspace direcory
```bash
cd ~/msl_robot/msl_robot_ws
```
Build te project:
```bash
colcon build --symlink-install
source install/setup.bash
```

### Running the Project
Make sure you are in the workspace direcory and run:
```bash
ros2 launch msl_robot_description msl_robot.launch.py
```
