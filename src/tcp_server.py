#!/usr/bin/env Python3
import rospy
from geometry_msgs.msg import Twist
import socket
import json

class TCP_Server():

    def __init__(self, ip, port, BUFFER_SIZE=1024):

        self.ip   = ip
        self.port = port
        self.data = Twist()
        self.buffer_size = BUFFER_SIZE
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock.listen(1)


    def run(self):
        msg = dict()
        while True:
            conn, addr = self.sock.accept()
            try:
                print('Connection address: {} '.format(addr))
                while(True):
                    msg = json.loads(conn.recv(self.buffer_size))
                    if msg:
                        self.data = self.convert_dict_2_twist(msg)
                        print('data receivded from bot1:\n ', self.data)

                    else:
                        print('no more data')
                        break
            except KeyboardInterrupt:
                conn.close()
                break
            finally:
                conn.close()
                break
    
    def convert_dict_2_twist(self, msg):
        temp = Twist()
        temp.linear.x = msg['linear']['x']
        temp.linear.y = msg['linear']['y']
        temp.linear.z = msg['linear']['z']
        temp.angular.x = msg['angular']['x']
        temp.angular.y = msg['angular']['y']
        temp.angular.z = msg['angular']['z']
        return temp


server = None

def main():
    global server
    server = TCP_Server(ip='127.0.0.1', port=5000)
    rospy.init_node(name='tcp_server_node', anonymous=True)
    server.run()

if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        rospy.loginfo('shutdown')


    