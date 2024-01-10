from setuptools import find_packages, setup
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'robot_arm_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name), glob('urdf/*')),
        (os.path.join('share', package_name), glob('config.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='James Randall',
    maintainer_email='randallj24@student.jhs.net',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
