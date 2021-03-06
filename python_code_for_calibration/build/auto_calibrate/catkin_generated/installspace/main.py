#!/usr/bin/env python2

from encodings import utf_8
import time
import rospy
from std_msgs.msg import String
import moveit_commander
import moveit_msgs.msg
import sys


class MoveGroupTutorial(object):
    def __init__(self):
        super(MoveGroupTutorial, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('test_move', anonymous=True)
        robot=moveit_commander.RobotCommander()
        scene=moveit_commander.PlanningSceneInterface()
        group_name="manipulator"
        group=moveit_commander.MoveGroupCommander(group_name)
        display_trajectory_publisher=rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
        planning_frame=group.get_planning_frame()
        print ("============ Reference frame: %s" % planning_frame)
        eef_link = group.get_end_effector_link()
        print "============ End effector: %s" % eef_link
        group_names = robot.get_group_names()
        print "============ Robot Groups:", robot.get_group_names()
        print "============ Printing robot state"
        print robot.get_current_state()
        print ""

        self.box_name = ''
        self.robot = robot
        self.scene = scene
        self.group = group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names
        # self.track_flag=False
        # self.default_pose_flag=True
        self.cx=400.0
        self.cy=400.0
        self.bridge=cv_bridge.CvBridge()
        self.image_sub=rospy.Subscriber('/camera/color/image_raw', Image, image_callback)

    # def go_to_ready_pose(self):
    #     group=self.group
    #     joint_goal=group.get_current_joint_values()
    #     print(type(joint_goal), joint_goal)

    #     joint_goal[0]= pi * 0.5
    #     joint_goal[1]= -pi * 0.5
    #     joint_goal[2]= -pi * 0.5
    #     joint_goal[3]= -pi * 0.5
    #     joint_goal[4]= pi * 0.5
    #     joint_goal[5]= 0

    #     group.go(joint_goal, wait=True)
    #     group.stop()
    #     current_joints=self.group.get_current_joint_values()
    #     return all_close(joint_goal, current_joints, 0.01)

def talker():
    runAgain = True
    while(runAgain):
        pub = rospy.Publisher(
            '/ur_hardware_interface/script_command', String, queue_size=1000000)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(125)  # 10hz
        hello_str = "freedrive_mode()"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

        val = raw_input("run again? Y or N : ")
        val = val.lower()
        if(val == "y"):
            print("running program again")
            runAgain = True
        else:
            print("printint robot pos ")
            getRobotPos()
            print("done getting robot pose")
            hello_str = "end_freedrive_mode()"
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
            time.sleep(2)
            rospy.on_shutdown("program ending")
            runAgain = False

def getRobotPos():
    group=self.group
    moveit_commander.roscpp_initialize(sys.argv)
    robot=moveit_commander.RobotCommander()
    print(group.current_joint_values())
    return

if __name__ == '__main__':
    try:
        tutorial=MoveGroupTutorial()
        talker()
    except rospy.ROSInterruptException:
        pass


