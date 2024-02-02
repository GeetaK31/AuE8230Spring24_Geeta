#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move_square():
	# Starts a new node
	rospy.init_node('robot_cleaner', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel_msg = Twist()

	# Set the linear velocity in the x-axis
	speed = 0.2
	# Set the angular velocity in the z-axis
	angular_speed = 0.2
	size = 2.0
    
	while not rospy.is_shutdown():

		# Loop to move the turtle in a square
		for i in range(4):
			# Publish the velocity
			vel_msg.linear.x = speed
			vel_msg.angular.z = 0
			
			t0 = rospy.Time.now().to_sec()
			current_distance = 0
			
			while(current_distance<size):
				velocity_publisher.publish(vel_msg)
				t1 = rospy.Time.now().to_sec()
				current_distance = speed*(t1-t0)
			vel_msg.linear.x = 0


			velocity_publisher.publish(vel_msg)

			# Turn the tu0rtle by 90 degrees
			vel_msg.linear.x = 0
			vel_msg.angular.z = angular_speed
			
			t0 = rospy.Time.now().to_sec()
			relative_angle = 0
			
			while(relative_angle<math.pi/2):
				velocity_publisher.publish(vel_msg)
				t1 = rospy.Time.now().to_sec()
				relative_angle = angular_speed*(t1-t0)

			vel_msg.linear.x =0
			vel_msg.angular.z = 0
			velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        # Testing our function
        move_square()
    except rospy.ROSInterruptException: pass

