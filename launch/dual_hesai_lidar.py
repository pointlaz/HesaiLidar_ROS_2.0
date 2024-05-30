from launch import LaunchDescription
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os
from launch_ros.substitutions import FindPackageShare

def generate_launch_description(): 
    ld = LaunchDescription()

    launch_args = [
        DeclareLaunchArgument('open_rviz', default_value='false'),
        DeclareLaunchArgument('lidar_0_namespace', default_value='lidar_0_hesai'),
        DeclareLaunchArgument('lidar_0_server_ip', default_value='192.168.1.201'),
        DeclareLaunchArgument('lidar_0_recv_port', default_value='2368'),
        DeclareLaunchArgument('lidar_0_gps_port', default_value='10110'),
        DeclareLaunchArgument('lidar_0_frame_id', default_value='lidar_0'),
        DeclareLaunchArgument('lidar_1_namespace', default_value='lidar_1_hesai'),
        DeclareLaunchArgument('lidar_1_server_ip', default_value='192.168.2.201'),
        DeclareLaunchArgument('lidar_1_recv_port', default_value='2369'),
        DeclareLaunchArgument('lidar_1_gps_port', default_value='10110'),
        DeclareLaunchArgument('lidar_1_frame_id', default_value='lidar_1'),
        DeclareLaunchArgument('pcap_file', default_value=''),
        DeclareLaunchArgument('start_angle', default_value='0'),
        DeclareLaunchArgument('lidar_type', default_value='PandarXT-32'),
        DeclareLaunchArgument('pcldata_type', default_value='0'),
        DeclareLaunchArgument('publish_type', default_value='points'),
        DeclareLaunchArgument('timestamp_type', default_value=''),
        DeclareLaunchArgument('data_type', default_value=''),
        DeclareLaunchArgument('lidar_correction_file', default_value=os.path.join(hesai_lidar_share_dir, 'config', 'PandarXT-32.csv')),
        DeclareLaunchArgument('multicast_ip', default_value=''),
        DeclareLaunchArgument('coordinate_correction_flag', default_value='false'),
        DeclareLaunchArgument('fixed_frame', default_value=''),
        DeclareLaunchArgument('target_frame', default_value=''),
        DeclareLaunchArgument('standby', default_value='false'),
    ]

    lidar_0_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource([FindPackageShare(hesai_ros_driver), '/launch', 'start.py']), 
        launch_arguments={
            'namespace': LaunchConfiguration('lidar_0_namespace'),
            'server_ip': LaunchConfiguration('lidar_0_server_ip'),
            'lidar_recv_port': LaunchConfiguration('lidar_0_recv_port'),
            'gps_port': LaunchConfiguration('lidar_0_gps_port'),
            'frame_id': LaunchConfiguration('lidar_0_frame_id'),
            'pcap_file': LaunchConfiguration('pcap_file'),
            'start_angle': LaunchConfiguration('start_angle'),
            'lidar_type': LaunchConfiguration('lidar_type'),
            'pcldata_type': LaunchConfiguration('pcldata_type'),
            'publish_type': LaunchConfiguration('publish_type'),
            'timestamp_type': LaunchConfiguration('timestamp_type'),
            'data_type': LaunchConfiguration('data_type'),
            'lidar_correction_file': LaunchConfiguration('lidar_correction_file'),
            'multicast_ip': LaunchConfiguration('multicast_ip'),
            'coordinate_correction_flag': LaunchConfiguration('coordinate_correction_flag'),
            'fixed_frame': LaunchConfiguration('fixed_frame'),
            'target_frame': LaunchConfiguration('target_frame'),
            'standby': LaunchConfiguration('standby'),
        }.items()
        )
    
    lidar_1_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([FindPackageShare(hesai_ros_driver), 'launch', 'hesai_lidar_launch.py']),
        launch_arguments={
            'namespace': LaunchConfiguration('lidar_1_namespace'),
            'server_ip': LaunchConfiguration('lidar_1_server_ip'),
            'lidar_recv_port': LaunchConfiguration('lidar_1_recv_port'),
            'gps_port': LaunchConfiguration('lidar_1_gps_port'),
            'frame_id': LaunchConfiguration('lidar_1_frame_id'),
            'pcap_file': LaunchConfiguration('pcap_file'),
            'start_angle': LaunchConfiguration('start_angle'),
            'lidar_type': LaunchConfiguration('lidar_type'),
            'pcldata_type': LaunchConfiguration('pcldata_type'),
            'publish_type': LaunchConfiguration('publish_type'),
            'timestamp_type': LaunchConfiguration('timestamp_type'),
            'data_type': LaunchConfiguration('data_type'),
            'lidar_correction_file': LaunchConfiguration('lidar_correction_file'),
            'multicast_ip': LaunchConfiguration('multicast_ip'),
            'coordinate_correction_flag': LaunchConfiguration('coordinate_correction_flag'),
            'fixed_frame': LaunchConfiguration('fixed_frame'),
            'target_frame': LaunchConfiguration('target_frame'),
            'standby': LaunchConfiguration('standby'),
        }.items()
    )
    return LaunchDescription(launch_args + [lidar_0_launch, lidar_1_launch])
    

