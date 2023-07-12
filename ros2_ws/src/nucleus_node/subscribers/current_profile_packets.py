import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor

from interfaces.msg import CurrentProfile


class SubscriberCurrentProfilePackets(Node):

    def __init__(self, callback_function, topic='current_profile', qos_profile=100):

        super().__init__('subscriber_current_profile_packets')

        self.subscription = self.create_subscription(CurrentProfile, topic=topic, callback=callback_function, qos_profile=qos_profile)

    def subscribe(self):

        if self.executor is not None:
            self.executor.spin()
        else:
            self.get_logger().warning('This subscriber is not added to an executor. Establishing a temporary SingleThreadedExecutor for this subscription')
            executor = SingleThreadedExecutor()
            executor.add_node(self)
            executor.spin()
            executor.shutdown()

def main(args=None):

    def current_profile_packet_callback(current_profile):
        
        subscriber.get_logger().info(f'velocity_data: {current_profile.velocity_data}')
            
    rclpy.init(args=args)

    subscriber = SubscriberCurrentProfilePackets(callback_function=current_profile_packet_callback)

    executor = SingleThreadedExecutor()
    executor.add_node(subscriber)

    subscriber.subscribe()

    executor.shutdown()

    subscriber.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
