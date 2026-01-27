// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lhd_msgs:action/NavToWaypoint.idl
// generated code does not contain a copyright notice

#ifndef LHD_MSGS__ACTION__DETAIL__NAV_TO_WAYPOINT__BUILDER_HPP_
#define LHD_MSGS__ACTION__DETAIL__NAV_TO_WAYPOINT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lhd_msgs/action/detail/nav_to_waypoint__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_Goal_waypoints
{
public:
  Init_NavToWaypoint_Goal_waypoints()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lhd_msgs::action::NavToWaypoint_Goal waypoints(::lhd_msgs::action::NavToWaypoint_Goal::_waypoints_type arg)
  {
    msg_.waypoints = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_Goal>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_Goal_waypoints();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_Result_time_taken
{
public:
  Init_NavToWaypoint_Result_time_taken()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lhd_msgs::action::NavToWaypoint_Result time_taken(::lhd_msgs::action::NavToWaypoint_Result::_time_taken_type arg)
  {
    msg_.time_taken = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_Result>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_Result_time_taken();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_Feedback_current_x_y_theta
{
public:
  Init_NavToWaypoint_Feedback_current_x_y_theta()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lhd_msgs::action::NavToWaypoint_Feedback current_x_y_theta(::lhd_msgs::action::NavToWaypoint_Feedback::_current_x_y_theta_type arg)
  {
    msg_.current_x_y_theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_Feedback>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_Feedback_current_x_y_theta();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_SendGoal_Request_goal
{
public:
  explicit Init_NavToWaypoint_SendGoal_Request_goal(::lhd_msgs::action::NavToWaypoint_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::NavToWaypoint_SendGoal_Request goal(::lhd_msgs::action::NavToWaypoint_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_SendGoal_Request msg_;
};

class Init_NavToWaypoint_SendGoal_Request_goal_id
{
public:
  Init_NavToWaypoint_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavToWaypoint_SendGoal_Request_goal goal_id(::lhd_msgs::action::NavToWaypoint_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_NavToWaypoint_SendGoal_Request_goal(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_SendGoal_Request>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_SendGoal_Request_goal_id();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_SendGoal_Response_stamp
{
public:
  explicit Init_NavToWaypoint_SendGoal_Response_stamp(::lhd_msgs::action::NavToWaypoint_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::NavToWaypoint_SendGoal_Response stamp(::lhd_msgs::action::NavToWaypoint_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_SendGoal_Response msg_;
};

class Init_NavToWaypoint_SendGoal_Response_accepted
{
public:
  Init_NavToWaypoint_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavToWaypoint_SendGoal_Response_stamp accepted(::lhd_msgs::action::NavToWaypoint_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_NavToWaypoint_SendGoal_Response_stamp(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_SendGoal_Response>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_SendGoal_Response_accepted();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_GetResult_Request_goal_id
{
public:
  Init_NavToWaypoint_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lhd_msgs::action::NavToWaypoint_GetResult_Request goal_id(::lhd_msgs::action::NavToWaypoint_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_GetResult_Request>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_GetResult_Request_goal_id();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_GetResult_Response_result
{
public:
  explicit Init_NavToWaypoint_GetResult_Response_result(::lhd_msgs::action::NavToWaypoint_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::NavToWaypoint_GetResult_Response result(::lhd_msgs::action::NavToWaypoint_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_GetResult_Response msg_;
};

class Init_NavToWaypoint_GetResult_Response_status
{
public:
  Init_NavToWaypoint_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavToWaypoint_GetResult_Response_result status(::lhd_msgs::action::NavToWaypoint_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_NavToWaypoint_GetResult_Response_result(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_GetResult_Response>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_GetResult_Response_status();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_NavToWaypoint_FeedbackMessage_feedback
{
public:
  explicit Init_NavToWaypoint_FeedbackMessage_feedback(::lhd_msgs::action::NavToWaypoint_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::NavToWaypoint_FeedbackMessage feedback(::lhd_msgs::action::NavToWaypoint_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_FeedbackMessage msg_;
};

class Init_NavToWaypoint_FeedbackMessage_goal_id
{
public:
  Init_NavToWaypoint_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavToWaypoint_FeedbackMessage_feedback goal_id(::lhd_msgs::action::NavToWaypoint_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_NavToWaypoint_FeedbackMessage_feedback(msg_);
  }

private:
  ::lhd_msgs::action::NavToWaypoint_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::NavToWaypoint_FeedbackMessage>()
{
  return lhd_msgs::action::builder::Init_NavToWaypoint_FeedbackMessage_goal_id();
}

}  // namespace lhd_msgs

#endif  // LHD_MSGS__ACTION__DETAIL__NAV_TO_WAYPOINT__BUILDER_HPP_
