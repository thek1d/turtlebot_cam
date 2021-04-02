## Launching Camera Module
- open 2 terminals
- specifiy robot model, "export TURTLEBOT3_MODEL=waffle"
- starting world with bot execute "roslaunch package_turtlebot_cam_ogu camera_world.launch"
- starting camera and <b>teleop node</b> execute "roslaunch package_turtlebot_cam_ogu collaborate_comm.launch"

## Lauching Communication Module
- open 2 terminals
- specifiy robot model, "export TURTLEBOT3_MODEL=waffle"
- to start world and <b>teleop_node for bot1</b> execute "roslaunch package_turtlebot_cam_ogu collaborate_world.launch"
- for running communication via TCP execute "roslaunch package_turtlebot_cam_ogu collaborate_comm.launch" in other terminal