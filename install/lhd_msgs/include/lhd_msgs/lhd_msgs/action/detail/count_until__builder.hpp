// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lhd_msgs:action/CountUntil.idl
// generated code does not contain a copyright notice

#ifndef LHD_MSGS__ACTION__DETAIL__COUNT_UNTIL__BUILDER_HPP_
#define LHD_MSGS__ACTION__DETAIL__COUNT_UNTIL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lhd_msgs/action/detail/count_until__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_Goal_period
{
public:
  explicit Init_CountUntil_Goal_period(::lhd_msgs::action::CountUntil_Goal & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::CountUntil_Goal period(::lhd_msgs::action::CountUntil_Goal::_period_type arg)
  {
    msg_.period = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_Goal msg_;
};

class Init_CountUntil_Goal_target_number
{
public:
  Init_CountUntil_Goal_target_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CountUntil_Goal_period target_number(::lhd_msgs::action::CountUntil_Goal::_target_number_type arg)
  {
    msg_.target_number = std::move(arg);
    return Init_CountUntil_Goal_period(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_Goal>()
{
  return lhd_msgs::action::builder::Init_CountUntil_Goal_target_number();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_Result_reached_number
{
public:
  Init_CountUntil_Result_reached_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lhd_msgs::action::CountUntil_Result reached_number(::lhd_msgs::action::CountUntil_Result::_reached_number_type arg)
  {
    msg_.reached_number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_Result>()
{
  return lhd_msgs::action::builder::Init_CountUntil_Result_reached_number();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_Feedback_current_number
{
public:
  Init_CountUntil_Feedback_current_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lhd_msgs::action::CountUntil_Feedback current_number(::lhd_msgs::action::CountUntil_Feedback::_current_number_type arg)
  {
    msg_.current_number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_Feedback>()
{
  return lhd_msgs::action::builder::Init_CountUntil_Feedback_current_number();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_SendGoal_Request_goal
{
public:
  explicit Init_CountUntil_SendGoal_Request_goal(::lhd_msgs::action::CountUntil_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::CountUntil_SendGoal_Request goal(::lhd_msgs::action::CountUntil_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_SendGoal_Request msg_;
};

class Init_CountUntil_SendGoal_Request_goal_id
{
public:
  Init_CountUntil_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CountUntil_SendGoal_Request_goal goal_id(::lhd_msgs::action::CountUntil_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_CountUntil_SendGoal_Request_goal(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_SendGoal_Request>()
{
  return lhd_msgs::action::builder::Init_CountUntil_SendGoal_Request_goal_id();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_SendGoal_Response_stamp
{
public:
  explicit Init_CountUntil_SendGoal_Response_stamp(::lhd_msgs::action::CountUntil_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::CountUntil_SendGoal_Response stamp(::lhd_msgs::action::CountUntil_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_SendGoal_Response msg_;
};

class Init_CountUntil_SendGoal_Response_accepted
{
public:
  Init_CountUntil_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CountUntil_SendGoal_Response_stamp accepted(::lhd_msgs::action::CountUntil_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_CountUntil_SendGoal_Response_stamp(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_SendGoal_Response>()
{
  return lhd_msgs::action::builder::Init_CountUntil_SendGoal_Response_accepted();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_GetResult_Request_goal_id
{
public:
  Init_CountUntil_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lhd_msgs::action::CountUntil_GetResult_Request goal_id(::lhd_msgs::action::CountUntil_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_GetResult_Request>()
{
  return lhd_msgs::action::builder::Init_CountUntil_GetResult_Request_goal_id();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_GetResult_Response_result
{
public:
  explicit Init_CountUntil_GetResult_Response_result(::lhd_msgs::action::CountUntil_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::CountUntil_GetResult_Response result(::lhd_msgs::action::CountUntil_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_GetResult_Response msg_;
};

class Init_CountUntil_GetResult_Response_status
{
public:
  Init_CountUntil_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CountUntil_GetResult_Response_result status(::lhd_msgs::action::CountUntil_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_CountUntil_GetResult_Response_result(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_GetResult_Response>()
{
  return lhd_msgs::action::builder::Init_CountUntil_GetResult_Response_status();
}

}  // namespace lhd_msgs


namespace lhd_msgs
{

namespace action
{

namespace builder
{

class Init_CountUntil_FeedbackMessage_feedback
{
public:
  explicit Init_CountUntil_FeedbackMessage_feedback(::lhd_msgs::action::CountUntil_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::lhd_msgs::action::CountUntil_FeedbackMessage feedback(::lhd_msgs::action::CountUntil_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_FeedbackMessage msg_;
};

class Init_CountUntil_FeedbackMessage_goal_id
{
public:
  Init_CountUntil_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CountUntil_FeedbackMessage_feedback goal_id(::lhd_msgs::action::CountUntil_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_CountUntil_FeedbackMessage_feedback(msg_);
  }

private:
  ::lhd_msgs::action::CountUntil_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::lhd_msgs::action::CountUntil_FeedbackMessage>()
{
  return lhd_msgs::action::builder::Init_CountUntil_FeedbackMessage_goal_id();
}

}  // namespace lhd_msgs

#endif  // LHD_MSGS__ACTION__DETAIL__COUNT_UNTIL__BUILDER_HPP_
