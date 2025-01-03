import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Float32, "kane", 10)
        self.create_timer(1.0, self.cb)
        self.n = 0.0
        self.m = 0.0


    def cb(self):
        msg = Float32()
        msg.data = float(int(self.n))
        self.pub.publish(msg)
        self.m += 1.0
        self.n = 100000.0 * 0.18 / 365.0 * self.m

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
