#!/usr/bin/env python 

import rospy 
import os


def getParam():
	planner_state =rospy.get_param("/move_base/GlobalPlanner/use_dijkstra")
	print(planner_state)
def changeParam():
	#rospy.set_param('/move_base/GlobalPlanner/use_dijkstra','false')
	os.system("rosparam set /move_base/GlobalPlanner/use_dijkstra false")
	getParam()
def startLaunch():
		os.system("roslaunch botpackage Sim_Launch_Compact.launch")
		getParam()




if __name__ =="__main__":
	
	#getParam()
	changeParam()
	startLaunch()
	
	
