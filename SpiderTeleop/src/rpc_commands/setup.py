from setuptools import find_packages, setup

package_name = 'rpc_commands'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wshengggg',
    maintainer_email='wsjasonteh2003@gmail.com',
    description='This is a ROS package for controlling HiWonder SpiderPi with JSON-RPC commands',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'rteleop = rpc_commands.rteleop:main',
        'navigation_demo = rpc_commands.navigation_demo:main',
        ],
    },
)
