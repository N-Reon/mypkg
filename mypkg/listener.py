# SPDX-FileCopyRightText: 2024 Reon Nuki s23c1102ek@s.chibakoudai.jp
# SPDX-Licence-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


rclpy.init()
node = Node("listener")


def cd(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def main():
    sub = node.create_subscription(Float32, "kane", cd, 10)
    rclpy.spin(node)
