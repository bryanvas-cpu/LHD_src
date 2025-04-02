cmake_minimum_required(VERSION 3.8)
project(lhd_automation)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(lhd_msgs REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2 REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
    ${PROJECT_NAME}/lhd_client.py
    ${PROJECT_NAME}/lhd_server.py
    ${PROJECT_NAME}/path_planning_service.py
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
