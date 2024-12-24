import rclpy
from rclpy.node import Node
from std_msgs.msg import Float16

class Talker(Node):
    def __init__(salf):
        super().__init__("talker")
        self.pub = self.create_publisher(Float16, "countup", 10)
        self.create_timer(1.0, self.cd)
        self.n = 0.0
        self.m = 0.0


    def cb(self):
        global n
        msg = Float16()
        msg.data = self.n
        self.pub.publish(msg)
        self.m += 1.0
        self.n = 100000.0 * 0.18 / 365.0 * self.m

def main():
    node.create_timer(1.0, cb)
    rclpy.spin(node)
