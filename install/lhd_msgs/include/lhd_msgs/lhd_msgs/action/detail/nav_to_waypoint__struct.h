// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from lhd_msgs:action/NavToWaypoint.idl
// generated code does not contain a copyright notice

#ifndef LHD_MSGS__ACTION__DETAIL__NAV_TO_WAYPOINT__STRUCT_H_
#define LHD_MSGS__ACTION__DETAIL__NAV_TO_WAYPOINT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'waypoints'
#include "geometry_msgs/msg/detail/pose_array__struct.h"

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_Goal
{
  geometry_msgs__msg__PoseArray waypoints;
} lhd_msgs__action__NavToWaypoint_Goal;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_Goal.
typedef struct lhd_msgs__action__NavToWaypoint_Goal__Sequence
{
  lhd_msgs__action__NavToWaypoint_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_Result
{
  float time_taken;
} lhd_msgs__action__NavToWaypoint_Result;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_Result.
typedef struct lhd_msgs__action__NavToWaypoint_Result__Sequence
{
  lhd_msgs__action__NavToWaypoint_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'current_x_y_theta'
#include "std_msgs/msg/detail/float64_multi_array__struct.h"

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_Feedback
{
  /// [x, y, theta]
  std_msgs__msg__Float64MultiArray current_x_y_theta;
} lhd_msgs__action__NavToWaypoint_Feedback;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_Feedback.
typedef struct lhd_msgs__action__NavToWaypoint_Feedback__Sequence
{
  lhd_msgs__action__NavToWaypoint_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "lhd_msgs/action/detail/nav_to_waypoint__struct.h"

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  lhd_msgs__action__NavToWaypoint_Goal goal;
} lhd_msgs__action__NavToWaypoint_SendGoal_Request;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_SendGoal_Request.
typedef struct lhd_msgs__action__NavToWaypoint_SendGoal_Request__Sequence
{
  lhd_msgs__action__NavToWaypoint_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} lhd_msgs__action__NavToWaypoint_SendGoal_Response;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_SendGoal_Response.
typedef struct lhd_msgs__action__NavToWaypoint_SendGoal_Response__Sequence
{
  lhd_msgs__action__NavToWaypoint_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} lhd_msgs__action__NavToWaypoint_GetResult_Request;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_GetResult_Request.
typedef struct lhd_msgs__action__NavToWaypoint_GetResult_Request__Sequence
{
  lhd_msgs__action__NavToWaypoint_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "lhd_msgs/action/detail/nav_to_waypoint__struct.h"

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_GetResult_Response
{
  int8_t status;
  lhd_msgs__action__NavToWaypoint_Result result;
} lhd_msgs__action__NavToWaypoint_GetResult_Response;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_GetResult_Response.
typedef struct lhd_msgs__action__NavToWaypoint_GetResult_Response__Sequence
{
  lhd_msgs__action__NavToWaypoint_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "lhd_msgs/action/detail/nav_to_waypoint__struct.h"

/// Struct defined in action/NavToWaypoint in the package lhd_msgs.
typedef struct lhd_msgs__action__NavToWaypoint_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  lhd_msgs__action__NavToWaypoint_Feedback feedback;
} lhd_msgs__action__NavToWaypoint_FeedbackMessage;

// Struct for a sequence of lhd_msgs__action__NavToWaypoint_FeedbackMessage.
typedef struct lhd_msgs__action__NavToWaypoint_FeedbackMessage__Sequence
{
  lhd_msgs__action__NavToWaypoint_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lhd_msgs__action__NavToWaypoint_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LHD_MSGS__ACTION__DETAIL__NAV_TO_WAYPOINT__STRUCT_H_
