// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from lhd_msgs:srv/GetWaypoints.idl
// generated code does not contain a copyright notice

#ifndef LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__STRUCT_H_
#define LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'start'
// Member 'end'
#include "geometry_msgs/msg/detail/pose__struct.h"

/// Struct defined in srv/GetWaypoints in the package lhd_msgs.
typedef struct lhd_msgs__srv__GetWaypoints_Request
{
  geometry_msgs__msg__Pose start;
  geometry_msgs__msg__Pose end;
} lhd_msgs__srv__GetWaypoints_Request;

// Struct for a sequence of lhd_msgs__srv__GetWaypoints_Request.
typedef struct lhd_msgs__srv__GetWaypoints_Request__Sequence
{
  lhd_msgs__srv__GetWaypoints_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__srv__GetWaypoints_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'waypoints'
#include "geometry_msgs/msg/detail/pose_array__struct.h"

/// Struct defined in srv/GetWaypoints in the package lhd_msgs.
typedef struct lhd_msgs__srv__GetWaypoints_Response
{
  geometry_msgs__msg__PoseArray waypoints;
  bool success;
} lhd_msgs__srv__GetWaypoints_Response;

// Struct for a sequence of lhd_msgs__srv__GetWaypoints_Response.
typedef struct lhd_msgs__srv__GetWaypoints_Response__Sequence
{
  lhd_msgs__srv__GetWaypoints_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__srv__GetWaypoints_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LHD_MSGS__SRV__DETAIL__GET_WAYPOINTS__STRUCT_H_
