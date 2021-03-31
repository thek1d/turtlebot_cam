import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def image_cb(ros_img, brigde):
    try:
        cv_image = brigde.imgmsg_to_cv2(ros_img, desired_encoding='bgr8')
    except CvBridgeError as e:
        print(e)
    show_img(cv_image)

def show_img(cv_image):
    cv2.imshow('waffle_stream', cv_image)
    cv2.waitKey(10)

def main():
    rospy.init_node('cam_node', anonymous=True)
    brigde = CvBridge()
    rospy.Subscriber(name='/camera/rgb/image_raw', data_class=Image, callback=image_cb, \
                     callback_args=brigde, queue_size=1)

if __name__=='__main__':
    main()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        cv2.destroyAllWindows()