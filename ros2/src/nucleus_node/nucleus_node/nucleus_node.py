import rclpy
from rclpy.node import Node
from nucleus_driver import NucleusDriver

class NucleusDriverRos:

    def __init__(self) -> None:
        
        self.nucleus_driver = NucleusDriver()

        #rospy.Subscriber()

    def connect_tcp(self, host, password=None):

        self.nucleus_driver.set_tcp_configuration(host=host)
        return self.nucleus_driver.connect(connection_type='tcp', password=password)

    def connect_serial(self, port):

        self.nucleus_driver.set_serial_configuration(port=port)
        return self.nucleus_driver.connect(connection_type='serial')

    def disconnect(self):

        return self.nucleus_driver.disconnect()

    def start(self):

        return self.nucleus_driver.start_measurement()

    def stop(self):

        return self.nucleus_driver.stop()

    def get_packet(self):

        return self.nucleus_driver.read_packet()

class NucleusNode(Node):

    def __init__(self, nucleus_driver):
        super().__init__("nucleus_connect")

        self.nucleus_driver = nucleus_driver

        self.get_logger().info('Hello from connect node')
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('timer')


def main():
    print('Hi from nucleus_driver.')

    nucleus_driver = NucleusDriver()

    rclpy.init(args=args)

    nucleus_node = NucleusNode(nucleus_driver=nucleus_driver)
    rclpy.spin(nucleus_node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
