from setuptools import setup, find_packages
from glob import glob
import os

package_name = '5Glocalization'

setup(
    name=package_name,
    version='0.0.0',
     packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='brendofernandes',
    maintainer_email='brendofernandes@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publisher1 = 5Glocalization.publisher1:main",
            "subscriber1 = 5Glocalization.subscriber1:main",
            "node = 5Glocalization.node:main",
            "move = 5Glocalization.move:main",
            "pub_modbus = 5Glocalization.pub_modbus:main",
            "sub_modbus = 5Glocalization.sub_modbus:main",
            "modbus_server = 5Glocalization.modbus_server:main"
        
        ],
    },
)
