// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from lhd_msgs:srv/GetWaypoints.idl
// generated code does not contain a copyright notice

#ifndef LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__TRAITS_HPP_
#define LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "lhd_msgs/srv/detail/get_waypoints__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'start'
// Member 'end'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace lhd_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetWaypoints_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: start
  {
    out << "start: ";
    to_flow_style_yaml(msg.start, out);
    out << ", ";
  }

  // member: end
  {
    out << "end: ";
    to_flow_style_yaml(msg.end, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetWaypoints_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start:\n";
    to_block_style_yaml(msg.start, out, indentation + 2);
  }

  // member: end
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "end:\n";
    to_block_style_yaml(msg.end, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetWaypoints_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace lhd_msgs

namespace rosidl_generator_traits
{

[[deprecated("use lhd_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const lhd_msgs::srv::GetWaypoints_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  lhd_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use lhd_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const lhd_msgs::srv::GetWaypoints_Request & msg)
{
  return lhd_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<lhd_msgs::srv::GetWaypoints_Request>()
{
  return "lhd_msgs::srv::GetWaypoints_Request";
}

template<>
inline const char * name<lhd_msgs::srv::GetWaypoints_Request>()
{
  return "lhd_msgs/srv/GetWaypoints_Request";
}

template<>
struct has_fixed_size<lhd_msgs::srv::GetWaypoints_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct has_bounded_size<lhd_msgs::srv::GetWaypoints_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Pose>::value> {};

template<>
struct is_message<lhd_msgs::srv::GetWaypoints_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'waypoints'
#include "geometry_msgs/msg/detail/pose_array__traits.hpp"

namespace lhd_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetWaypoints_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: waypoints
  {
    out << "waypoints: ";
    to_flow_style_yaml(msg.waypoints, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetWaypoints_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: waypoints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoints:\n";
    to_block_style_yaml(msg.waypoints, out, indentation + 2);
  }

  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetWaypoints_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace lhd_msgs

namespace rosidl_generator_traits
{

[[deprecated("use lhd_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const lhd_msgs::srv::GetWaypoints_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  lhd_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use lhd_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const lhd_msgs::srv::GetWaypoints_Response & msg)
{
  return lhd_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<lhd_msgs::srv::GetWaypoints_Response>()
{
  return "lhd_msgs::srv::GetWaypoints_Response";
}

template<>
inline const char * name<lhd_msgs::srv::GetWaypoints_Response>()
{
  return "lhd_msgs/srv/GetWaypoints_Response";
}

template<>
struct has_fixed_size<lhd_msgs::srv::GetWaypoints_Response>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::PoseArray>::value> {};

template<>
struct has_bounded_size<lhd_msgs::srv::GetWaypoints_Response>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::PoseArray>::value> {};

template<>
struct is_message<lhd_msgs::srv::GetWaypoints_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<lhd_msgs::srv::GetWaypoints>()
{
  return "lhd_msgs::srv::GetWaypoints";
}

template<>
inline const char * name<lhd_msgs::srv::GetWaypoints>()
{
  return "lhd_msgs/srv/GetWaypoints";
}

template<>
struct has_fixed_size<lhd_msgs::srv::GetWaypoints>
  : std::integral_constant<
    bool,
    has_fixed_size<lhd_msgs::srv::GetWaypoints_Request>::value &&
    has_fixed_size<lhd_msgs::srv::GetWaypoints_Response>::value
  >
{
};

template<>
struct has_bounded_size<lhd_msgs::srv::GetWaypoints>
  : std::integral_constant<
    bool,
    has_bounded_size<lhd_msgs::srv::GetWaypoints_Request>::value &&
    has_bounded_size<lhd_msgs::srv::GetWaypoints_Response>::value
  >
{
};

template<>
struct is_service<lhd_msgs::srv::GetWaypoints>
  : std::true_type
{
};

template<>
struct is_service_request<lhd_msgs::srv::GetWaypoints_Request>
  : std::true_type
{
};

template<>
struct is_service_response<lhd_msgs::srv::GetWaypoints_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__TRAITS_HPP_
