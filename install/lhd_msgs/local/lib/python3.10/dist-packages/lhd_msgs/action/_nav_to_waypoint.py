# generated from rosidl_generator_py/resource/_idl.py.em
# with input from lhd_msgs:action/NavToWaypoint.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NavToWaypoint_Goal(type):
    """Metaclass of message 'NavToWaypoint_Goal'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__goal

            from geometry_msgs.msg import PoseArray
            if PoseArray.__class__._TYPE_SUPPORT is None:
                PoseArray.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_Goal(metaclass=Metaclass_NavToWaypoint_Goal):
    """Message class 'NavToWaypoint_Goal'."""

    __slots__ = [
        '_waypoints',
    ]

    _fields_and_field_types = {
        'waypoints': 'geometry_msgs/PoseArray',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseArray'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from geometry_msgs.msg import PoseArray
        self.waypoints = kwargs.get('waypoints', PoseArray())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.waypoints != other.waypoints:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def waypoints(self):
        """Message field 'waypoints'."""
        return self._waypoints

    @waypoints.setter
    def waypoints(self, value):
        if __debug__:
            from geometry_msgs.msg import PoseArray
            assert \
                isinstance(value, PoseArray), \
                "The 'waypoints' field must be a sub message of type 'PoseArray'"
        self._waypoints = value


# Import statements for member types

# already imported above
# import builtins

import math  # noqa: E402, I100

# already imported above
# import rosidl_parser.definition


class Metaclass_NavToWaypoint_Result(type):
    """Metaclass of message 'NavToWaypoint_Result'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__result

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_Result(metaclass=Metaclass_NavToWaypoint_Result):
    """Message class 'NavToWaypoint_Result'."""

    __slots__ = [
        '_time_taken',
    ]

    _fields_and_field_types = {
        'time_taken': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.time_taken = kwargs.get('time_taken', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.time_taken != other.time_taken:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def time_taken(self):
        """Message field 'time_taken'."""
        return self._time_taken

    @time_taken.setter
    def time_taken(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'time_taken' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'time_taken' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._time_taken = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavToWaypoint_Feedback(type):
    """Metaclass of message 'NavToWaypoint_Feedback'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__feedback

            from std_msgs.msg import Float64MultiArray
            if Float64MultiArray.__class__._TYPE_SUPPORT is None:
                Float64MultiArray.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_Feedback(metaclass=Metaclass_NavToWaypoint_Feedback):
    """Message class 'NavToWaypoint_Feedback'."""

    __slots__ = [
        '_current_x_y_theta',
    ]

    _fields_and_field_types = {
        'current_x_y_theta': 'std_msgs/Float64MultiArray',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Float64MultiArray'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Float64MultiArray
        self.current_x_y_theta = kwargs.get('current_x_y_theta', Float64MultiArray())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.current_x_y_theta != other.current_x_y_theta:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def current_x_y_theta(self):
        """Message field 'current_x_y_theta'."""
        return self._current_x_y_theta

    @current_x_y_theta.setter
    def current_x_y_theta(self, value):
        if __debug__:
            from std_msgs.msg import Float64MultiArray
            assert \
                isinstance(value, Float64MultiArray), \
                "The 'current_x_y_theta' field must be a sub message of type 'Float64MultiArray'"
        self._current_x_y_theta = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavToWaypoint_SendGoal_Request(type):
    """Metaclass of message 'NavToWaypoint_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__send_goal__request

            from lhd_msgs.action import NavToWaypoint
            if NavToWaypoint.Goal.__class__._TYPE_SUPPORT is None:
                NavToWaypoint.Goal.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_SendGoal_Request(metaclass=Metaclass_NavToWaypoint_SendGoal_Request):
    """Message class 'NavToWaypoint_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'lhd_msgs/NavToWaypoint_Goal',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['lhd_msgs', 'action'], 'NavToWaypoint_Goal'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Goal
        self.goal = kwargs.get('goal', NavToWaypoint_Goal())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Goal
            assert \
                isinstance(value, NavToWaypoint_Goal), \
                "The 'goal' field must be a sub message of type 'NavToWaypoint_Goal'"
        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavToWaypoint_SendGoal_Response(type):
    """Metaclass of message 'NavToWaypoint_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__send_goal__response

            from builtin_interfaces.msg import Time
            if Time.__class__._TYPE_SUPPORT is None:
                Time.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_SendGoal_Response(metaclass=Metaclass_NavToWaypoint_SendGoal_Response):
    """Message class 'NavToWaypoint_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
    ]

    _fields_and_field_types = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.accepted = kwargs.get('accepted', bool())
        from builtin_interfaces.msg import Time
        self.stamp = kwargs.get('stamp', Time())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self):
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'accepted' field must be of type 'bool'"
        self._accepted = value

    @builtins.property
    def stamp(self):
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value):
        if __debug__:
            from builtin_interfaces.msg import Time
            assert \
                isinstance(value, Time), \
                "The 'stamp' field must be a sub message of type 'Time'"
        self._stamp = value


class Metaclass_NavToWaypoint_SendGoal(type):
    """Metaclass of service 'NavToWaypoint_SendGoal'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__nav_to_waypoint__send_goal

            from lhd_msgs.action import _nav_to_waypoint
            if _nav_to_waypoint.Metaclass_NavToWaypoint_SendGoal_Request._TYPE_SUPPORT is None:
                _nav_to_waypoint.Metaclass_NavToWaypoint_SendGoal_Request.__import_type_support__()
            if _nav_to_waypoint.Metaclass_NavToWaypoint_SendGoal_Response._TYPE_SUPPORT is None:
                _nav_to_waypoint.Metaclass_NavToWaypoint_SendGoal_Response.__import_type_support__()


class NavToWaypoint_SendGoal(metaclass=Metaclass_NavToWaypoint_SendGoal):
    from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_SendGoal_Request as Request
    from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_SendGoal_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavToWaypoint_GetResult_Request(type):
    """Metaclass of message 'NavToWaypoint_GetResult_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__get_result__request

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_GetResult_Request(metaclass=Metaclass_NavToWaypoint_GetResult_Request):
    """Message class 'NavToWaypoint_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavToWaypoint_GetResult_Response(type):
    """Metaclass of message 'NavToWaypoint_GetResult_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__get_result__response

            from lhd_msgs.action import NavToWaypoint
            if NavToWaypoint.Result.__class__._TYPE_SUPPORT is None:
                NavToWaypoint.Result.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_GetResult_Response(metaclass=Metaclass_NavToWaypoint_GetResult_Response):
    """Message class 'NavToWaypoint_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
    ]

    _fields_and_field_types = {
        'status': 'int8',
        'result': 'lhd_msgs/NavToWaypoint_Result',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['lhd_msgs', 'action'], 'NavToWaypoint_Result'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.status = kwargs.get('status', int())
        from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Result
        self.result = kwargs.get('result', NavToWaypoint_Result())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'status' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'status' field must be an integer in [-128, 127]"
        self._status = value

    @builtins.property
    def result(self):
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value):
        if __debug__:
            from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Result
            assert \
                isinstance(value, NavToWaypoint_Result), \
                "The 'result' field must be a sub message of type 'NavToWaypoint_Result'"
        self._result = value


class Metaclass_NavToWaypoint_GetResult(type):
    """Metaclass of service 'NavToWaypoint_GetResult'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__nav_to_waypoint__get_result

            from lhd_msgs.action import _nav_to_waypoint
            if _nav_to_waypoint.Metaclass_NavToWaypoint_GetResult_Request._TYPE_SUPPORT is None:
                _nav_to_waypoint.Metaclass_NavToWaypoint_GetResult_Request.__import_type_support__()
            if _nav_to_waypoint.Metaclass_NavToWaypoint_GetResult_Response._TYPE_SUPPORT is None:
                _nav_to_waypoint.Metaclass_NavToWaypoint_GetResult_Response.__import_type_support__()


class NavToWaypoint_GetResult(metaclass=Metaclass_NavToWaypoint_GetResult):
    from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_GetResult_Request as Request
    from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_GetResult_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NavToWaypoint_FeedbackMessage(type):
    """Metaclass of message 'NavToWaypoint_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__nav_to_waypoint__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__nav_to_waypoint__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__nav_to_waypoint__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__nav_to_waypoint__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__nav_to_waypoint__feedback_message

            from lhd_msgs.action import NavToWaypoint
            if NavToWaypoint.Feedback.__class__._TYPE_SUPPORT is None:
                NavToWaypoint.Feedback.__class__.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID.__class__._TYPE_SUPPORT is None:
                UUID.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NavToWaypoint_FeedbackMessage(metaclass=Metaclass_NavToWaypoint_FeedbackMessage):
    """Message class 'NavToWaypoint_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
    ]

    _fields_and_field_types = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'lhd_msgs/NavToWaypoint_Feedback',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['lhd_msgs', 'action'], 'NavToWaypoint_Feedback'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from unique_identifier_msgs.msg import UUID
        self.goal_id = kwargs.get('goal_id', UUID())
        from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Feedback
        self.feedback = kwargs.get('feedback', NavToWaypoint_Feedback())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self):
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value):
        if __debug__:
            from unique_identifier_msgs.msg import UUID
            assert \
                isinstance(value, UUID), \
                "The 'goal_id' field must be a sub message of type 'UUID'"
        self._goal_id = value

    @builtins.property
    def feedback(self):
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        if __debug__:
            from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Feedback
            assert \
                isinstance(value, NavToWaypoint_Feedback), \
                "The 'feedback' field must be a sub message of type 'NavToWaypoint_Feedback'"
        self._feedback = value


class Metaclass_NavToWaypoint(type):
    """Metaclass of action 'NavToWaypoint'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('lhd_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'lhd_msgs.action.NavToWaypoint')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__nav_to_waypoint

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from lhd_msgs.action import _nav_to_waypoint
            if _nav_to_waypoint.Metaclass_NavToWaypoint_SendGoal._TYPE_SUPPORT is None:
                _nav_to_waypoint.Metaclass_NavToWaypoint_SendGoal.__import_type_support__()
            if _nav_to_waypoint.Metaclass_NavToWaypoint_GetResult._TYPE_SUPPORT is None:
                _nav_to_waypoint.Metaclass_NavToWaypoint_GetResult.__import_type_support__()
            if _nav_to_waypoint.Metaclass_NavToWaypoint_FeedbackMessage._TYPE_SUPPORT is None:
                _nav_to_waypoint.Metaclass_NavToWaypoint_FeedbackMessage.__import_type_support__()


class NavToWaypoint(metaclass=Metaclass_NavToWaypoint):

    # The goal message defined in the action definition.
    from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Goal as Goal
    # The result message defined in the action definition.
    from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Result as Result
    # The feedback message defined in the action definition.
    from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_Feedback as Feedback

    class Impl:

        # The send_goal service using a wrapped version of the goal message as a request.
        from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_SendGoal as SendGoalService
        # The get_result service using a wrapped version of the result message as a response.
        from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_GetResult as GetResultService
        # The feedback message with generic fields which wraps the feedback message.
        from lhd_msgs.action._nav_to_waypoint import NavToWaypoint_FeedbackMessage as FeedbackMessage

        # The generic service to cancel a goal.
        from action_msgs.srv._cancel_goal import CancelGoal as CancelGoalService
        # The generic message for get the status of a goal.
        from action_msgs.msg._goal_status_array import GoalStatusArray as GoalStatusMessage

    def __init__(self):
        raise NotImplementedError('Action classes can not be instantiated')
