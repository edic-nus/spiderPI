import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.ndimage import binary_dilation

class MapExpansionNode(Node):
    def __init__(self):
        super().__init__('map_expansion_node')
        self.subscription = self.create_subscription(
            OccupancyGrid,
            'map',
            self.map_callback,
            10)
        self.publisher = self.create_publisher(OccupancyGrid, 'expanded_map', 10)
        self.original_map_data = None
        self.expanded_map_data = None

        # Setup Matplotlib figure and axes
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 5))
        self.im1 = None
        self.im2 = None

        # Start the animation
        self.ani = FuncAnimation(self.fig, self.update_plot, interval=100)

    def map_callback(self, msg):
        self.original_map_data = np.array(msg.data).reshape((msg.info.height, msg.info.width))
        expanded_map = self.expand_map(msg)
        self.expanded_map_data = np.array(expanded_map.data).reshape((expanded_map.info.height, expanded_map.info.width))
        self.publisher.publish(expanded_map)

    def expand_map(self, msg):
        # Convert the map data to a numpy array
        map_data = np.array(msg.data).reshape((msg.info.height, msg.info.width))

        # Perform dilation (expansion) using a new algorithm
        expanded_map_data = self.dilate_map(map_data)

        # Create a new OccupancyGrid message for the expanded map
        expanded_map = OccupancyGrid()
        expanded_map.header = msg.header
        expanded_map.info = msg.info
        expanded_map.data = expanded_map_data.flatten().tolist()

        return expanded_map

    def dilate_map(self, map_data):
        # Threshold to consider a cell as occupied
        threshold = 50
        binary_map = map_data > threshold

        # Perform binary dilation
        dilated_binary_map = binary_dilation(binary_map, structure=np.ones((3, 3)))

        # Convert the dilated binary map back to occupancy values
        dilated_map = np.where(dilated_binary_map, 100, map_data)

        return dilated_map

    def update_plot(self, frame):
        if self.original_map_data is not None:
            if self.im1 is None:
                self.im1 = self.ax1.imshow(self.original_map_data, cmap='gray', vmin=-1, vmax=100)
                self.ax1.set_title('Original Map')
            else:
                self.im1.set_data(self.original_map_data)

        if self.expanded_map_data is not None:
            if self.im2 is None:
                self.im2 = self.ax2.imshow(self.expanded_map_data, cmap='gray', vmin=-1, vmax=100)
                self.ax2.set_title('Expanded Map')
            else:
                self.im2.set_data(self.expanded_map_data)

        self.fig.canvas.draw()

def main(args=None):
    rclpy.init(args=args)
    node = MapExpansionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    plt.show()
