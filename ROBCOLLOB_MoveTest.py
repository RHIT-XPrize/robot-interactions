import subprocess
import rospy
import intera_interface
import intera_interface.head_display as head
import cv2
import GraspingHelperClass as Gp
import sys
import time

############################################################
# This script takes the robot to pre-grasp position,
# takes a picture right on top of the workspace, and save it.
# This script is primarily used for debugging.
############################################################

def pickup_action(x, y):
  rospy.init_node("GraspingDemo")
  global limb
  limb = intera_interface.Limb('right')
  global gripper
  gripper = intera_interface.Gripper('right_gripper')

  # command
  gripper.open()
  headDisplay = head.HeadDisplay()
  rospy.sleep(1)
  # operation_x = Gp.in_to_m(25)
  operation_x = x
  # operation_y_1 = Gp.in_to_m(-19)
  operation_y_1 = y
  operation_y_2 = -1 * operation_y_1
  # Pre-grasping joint angles
  dQ = Gp.euler_to_quaternion(z=0)
  # print dQ
  operation_height_upper = 0.300
  # x = 36 inch, y = -18 inch
  camera_center_human_right = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_1, p_z=operation_height_upper,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  # x = 36 inch, y = 18 inch
  camera_center_human_left = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_2, p_z=operation_height_upper,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  moveComm = Gp.moveit_commander
  moveComm.roscpp_initialize(sys.argv)

  robot = moveComm.RobotCommander()
  scene = moveComm.PlanningSceneInterface()

  group_name = "right_arm"
  group = moveComm.MoveGroupCommander(group_name)
  display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   Gp.moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

  planning_frame = group.get_planning_frame()

  eef_link = group.get_end_effector_link()
  Gp.load_objects(scene, planning_frame)
  Gp.load_camera_w_mount(scene)

  # print limb.joint_angles()
  dQ = Gp.euler_to_quaternion(z=3.1415/2)
  # print dQ

  drop_block_pos = camera_center_human_right

  start = time.time()
  # command
  Gp.move_move(limb, group, drop_block_pos, 0.1)

  #go down sectionXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  dQ = Gp.euler_to_quaternion(z=0)
  operation_height_lower = 0.10
  camera_center_human_right = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_1, p_z=operation_height_lower,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  # x = 36 inch, y = 18 inch
  camera_center_human_left = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_2, p_z=operation_height_lower,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  moveComm = Gp.moveit_commander
  moveComm.roscpp_initialize(sys.argv)

  robot = moveComm.RobotCommander()
  scene = moveComm.PlanningSceneInterface()

  group_name = "right_arm"
  group = moveComm.MoveGroupCommander(group_name)
  display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   Gp.moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

  planning_frame = group.get_planning_frame()

  eef_link = group.get_end_effector_link()
  Gp.load_objects(scene, planning_frame)
  Gp.load_camera_w_mount(scene)

  # print limb.joint_angles()
  dQ = Gp.euler_to_quaternion(z=3.1415/2)

  drop_block_pos = camera_center_human_right

  start = time.time()
  # command
  Gp.move_move(limb, group, drop_block_pos, 0.1)
  gripper.close()


  #lift up section#############################################
  dQ = Gp.euler_to_quaternion(z=0)
  operation_height_lift = 0.500
  camera_center_human_right2 = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_1, p_z=operation_height_lift,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  # x = 36 inch, y = 18 inch
  camera_center_human_left2 = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_2, p_z=operation_height_lift,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  moveComm2 = Gp.moveit_commander
  moveComm2.roscpp_initialize(sys.argv)

  robot2 = moveComm2.RobotCommander()
  scene2 = moveComm2.PlanningSceneInterface()

  group_name2 = "right_arm"
  group2 = moveComm2.MoveGroupCommander(group_name2)
  display_trajectory_publisher2 = rospy.Publisher('/move_group/display_planned_path',
                                                   Gp.moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

  planning_frame2 = group2.get_planning_frame()

  eef_link2 = group2.get_end_effector_link()
  Gp.load_objects(scene, planning_frame)
  Gp.load_camera_w_mount(scene)

   # print limb.joint_angles()
  dQ = Gp.euler_to_quaternion(z=3.1415/2)



  #run groups

  Gp.move_move(limb, group2, camera_center_human_right2, 0.1)
  gripper.open()
  end = time.time()

  # print end - start

  rospy.sleep(1)


def point_action(x, y):
  rospy.init_node("GraspingDemo")
  global limb
  limb = intera_interface.Limb('right')
  global gripper
  gripper = intera_interface.Gripper('right_gripper')

  # command
  gripper.close()
  headDisplay = head.HeadDisplay()
  rospy.sleep(1)
  # operation_x = Gp.in_to_m(25)
  operation_x = x
  # operation_y_1 = Gp.in_to_m(-19)
  operation_y_1 = y
  operation_y_2 = -1 * operation_y_1
  # Pre-grasping joint angles
  dQ = Gp.euler_to_quaternion(z=0)
  # print dQ
  operation_height_upper = 0.300
  # x = 36 inch, y = -18 inch
  camera_center_human_right = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_1, p_z=operation_height_upper,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  # x = 36 inch, y = 18 inch
  camera_center_human_left = Gp.ik_service_client(limb='right', use_advanced_options=True,
                                              p_x=operation_x, p_y=operation_y_2, p_z=operation_height_upper,
                                              q_x=dQ[0], q_y=dQ[1], q_z=dQ[2], q_w=dQ[3])

  moveComm = Gp.moveit_commander
  moveComm.roscpp_initialize(sys.argv)

  robot = moveComm.RobotCommander()
  scene = moveComm.PlanningSceneInterface()

  group_name = "right_arm"
  group = moveComm.MoveGroupCommander(group_name)
  display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   Gp.moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

  planning_frame = group.get_planning_frame()

  eef_link = group.get_end_effector_link()
  Gp.load_objects(scene, planning_frame)
  Gp.load_camera_w_mount(scene)

  # print limb.joint_angles()
  dQ = Gp.euler_to_quaternion(z=3.1415/2)
  # print dQ

  drop_block_pos = camera_center_human_right

  start = time.time()
  # command
  Gp.move_move(limb, group, drop_block_pos, 0.1)
  rospy.sleep(1)
