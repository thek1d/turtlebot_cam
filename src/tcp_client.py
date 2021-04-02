#!/usr/bin/env Python3
import rospy
import socket
import json
from geometry_msgs.msg import Twist


class TCP_Client():
    
    def __init__(self, ip, port, BUFFER_SIZE=1024):
        self.ip = ip
        self.port = port
        self.rate = None
        self.data = None
        self.buffer = None
        self.buffer_size = BUFFER_SIZE
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
    
    def send_message(self, message):
        dict_msg = dict(dict())
        dict_msg = self.convert_twist_msg_2_dict(message)
        message = json.dumps(dict_msg).encode('utf-8')
        self.sock.send(message)
    
    def print_message(self):
        print('client received data: {}'.format(self.data))

    def convert_twist_msg_2_dict(self, message_twist):
        dict_msg = self.init_twist_dict()
        dict_msg['linear']['x']  = message_twist.linear.x
        dict_msg['linear']['y']  = message_twist.linear.y
        dict_msg['linear']['z']  = message_twist.linear.z
        dict_msg['angular']['x'] = message_twist.angular.x
        dict_msg['angular']['y'] = message_twist.angular.y
        dict_msg['angular']['z'] = message_twist.angular.z
        return dict_msg
    
    def init_twist_dict(self):
        dict_msg = { 'linear':{
                                    'x' : 0.0,
                                    'y' : 0.0,
                                    'z' : 0.0
                              },
                     'angular':{
                                    'x' : 0.0,
                                    'y' : 0.0,
                                    'z' : 0.0
                              }

        }
        return dict_msg
    
    
client = None

def bot0_cb(twist_msg):
    global client
    client.rate.sleep()
    client.send_message(twist_msg)

def main():
    global client
    client = TCP_Client(ip='127.0.0.1', port=5000)
    rospy.init_node(name='tcp_client_node', anonymous=True)
    bot0_sub = rospy.Subscriber(name='/bot0/cmd_vel', data_class=Twist, callback=bot0_cb, queue_size=1)
    client.rate = rospy.Rate(1)

if __name__ == '__main__':
    main()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print('shutdown')