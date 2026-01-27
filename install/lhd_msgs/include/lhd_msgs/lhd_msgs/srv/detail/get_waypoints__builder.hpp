// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lhd_msgs:srv/GetWaypoints.idl
// generated code does not contain a copyright notice

#ifndef LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__BUILDER_HPP_
#define LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lhd_msgs/srv/detail/get_waypoints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lhd_msgs
{

namespace srv
{

namespace builder
{

class Init_GetWaypoints_Request_end
{
public:
  explicit Init_GetWaypoints_Request_end(::lhd_msgs::srv::GetWaypoints_Request & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::srv::GetWaypoints_Request end(::lhd_msgs::srv::GetWaypoints_Request::_end_type arg)
  {
    msg_.end = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::srv::GetWaypoints_Request msg_;
};

class Init_GetWaypoints_Request_start
{
public:
  Init_GetWaypoints_Request_start()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetWaypoints_Request_end start(::lhd_msgs::srv::GetWaypoints_Request::_start_type arg)
  {
    msg_.start = std::move(arg);
    return Init_GetWaypoints_Request_end(msg_);
  }

private:
  ::lhd_msgs::srv::GetWaypoints_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::srv::GetWaypoints_Request>()
{
  return lhd_msgs::srv::builder::Init_GetWaypoints_Request_start();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace srv
{

namespace builder
{

class Init_GetWaypoints_Response_success
{
public:
  explicit Init_GetWaypoints_Response_success(::lhd_msgs::srv::GetWaypoints_Response & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::srv::GetWaypoints_Response success(::lhd_msgs::srv::GetWaypoints_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::srv::GetWaypoints_Response msg_;
};

class Init_GetWaypoints_Response_waypoints
{
public:
  Init_GetWaypoints_Response_waypoints()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetWaypoints_Response_success waypoints(::lhd_msgs::srv::GetWaypoints_Response::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return Init_GetWaypoints_Response_success(msg_);
  }

private:
  ::lhd_msgs::srv::GetWaypoints_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::srv::GetWaypoints_Response>()
{
  return lhd_msgs::srv::builder::Init_GetWaypoints_Response_waypoints();
}

}  // namespace lhd_msgs

#endif  // LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__BUILDER_HPP_
