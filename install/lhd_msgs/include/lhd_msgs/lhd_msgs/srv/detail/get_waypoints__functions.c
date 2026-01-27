// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from lhd_msgs:srv/GetWaypoints.idl
// generated code does not contain a copyright notice
#include "lhd_msgs/srv/detail/get_waypoints__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `start`
// Member `end`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
lhd_msgs__srv__GetWaypoints_Request__init(lhd_msgs__srv__GetWaypoints_Request * msg)
{
  if (!msg) {
    return false;
  }
  // start
  if (!geometry_msgs__msg__Pose__init(&msg->start)) {
    lhd_msgs__srv__GetWaypoints_Request__fini(msg);
    return false;
  }
  // end
  if (!geometry_msgs__msg__Pose__init(&msg->end)) {
    lhd_msgs__srv__GetWaypoints_Request__fini(msg);
    return false;
  }
  return true;
}

void
lhd_msgs__srv__GetWaypoints_Request__fini(lhd_msgs__srv__GetWaypoints_Request * msg)
{
  if (!msg) {
    return;
  }
  // start
  geometry_msgs__msg__Pose__fini(&msg->start);
  // end
  geometry_msgs__msg__Pose__fini(&msg->end);
}

bool
lhd_msgs__srv__GetWaypoints_Request__are_equal(const lhd_msgs__srv__GetWaypoints_Request * lhs, const lhd_msgs__srv__GetWaypoints_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // start
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->start), &(rhs->start)))
  {
    return false;
  }
  // end
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->end), &(rhs->end)))
  {
    return false;
  }
  return true;
}

bool
lhd_msgs__srv__GetWaypoints_Request__copy(
  const lhd_msgs__srv__GetWaypoints_Request * input,
  lhd_msgs__srv__GetWaypoints_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // start
  if (!geometry_msgs__msg__Pose__copy(
      &(input->start), &(output->start)))
  {
    return false;
  }
  // end
  if (!geometry_msgs__msg__Pose__copy(
      &(input->end), &(output->end)))
  {
    return false;
  }
  return true;
}

lhd_msgs__srv__GetWaypoints_Request *
lhd_msgs__srv__GetWaypoints_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lhd_msgs__srv__GetWaypoints_Request * msg = (lhd_msgs__srv__GetWaypoints_Request *)allocator.allocate(sizeof(lhd_msgs__srv__GetWaypoints_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(lhd_msgs__srv__GetWaypoints_Request));
  bool success = lhd_msgs__srv__GetWaypoints_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
lhd_msgs__srv__GetWaypoints_Request__destroy(lhd_msgs__srv__GetWaypoints_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    lhd_msgs__srv__GetWaypoints_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
lhd_msgs__srv__GetWaypoints_Request__Sequence__init(lhd_msgs__srv__GetWaypoints_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lhd_msgs__srv__GetWaypoints_Request * data = NULL;

  if (size) {
    data = (lhd_msgs__srv__GetWaypoints_Request *)allocator.zero_allocate(size, sizeof(lhd_msgs__srv__GetWaypoints_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = lhd_msgs__srv__GetWaypoints_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        lhd_msgs__srv__GetWaypoints_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
lhd_msgs__srv__GetWaypoints_Request__Sequence__fini(lhd_msgs__srv__GetWaypoints_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      lhd_msgs__srv__GetWaypoints_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

lhd_msgs__srv__GetWaypoints_Request__Sequence *
lhd_msgs__srv__GetWaypoints_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lhd_msgs__srv__GetWaypoints_Request__Sequence * array = (lhd_msgs__srv__GetWaypoints_Request__Sequence *)allocator.allocate(sizeof(lhd_msgs__srv__GetWaypoints_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = lhd_msgs__srv__GetWaypoints_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
lhd_msgs__srv__GetWaypoints_Request__Sequence__destroy(lhd_msgs__srv__GetWaypoints_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    lhd_msgs__srv__GetWaypoints_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
lhd_msgs__srv__GetWaypoints_Request__Sequence__are_equal(const lhd_msgs__srv__GetWaypoints_Request__Sequence * lhs, const lhd_msgs__srv__GetWaypoints_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!lhd_msgs__srv__GetWaypoints_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
lhd_msgs__srv__GetWaypoints_Request__Sequence__copy(
  const lhd_msgs__srv__GetWaypoints_Request__Sequence * input,
  lhd_msgs__srv__GetWaypoints_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(lhd_msgs__srv__GetWaypoints_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    lhd_msgs__srv__GetWaypoints_Request * data =
      (lhd_msgs__srv__GetWaypoints_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!lhd_msgs__srv__GetWaypoints_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          lhd_msgs__srv__GetWaypoints_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!lhd_msgs__srv__GetWaypoints_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `waypoints`
#include "geometry_msgs/msg/detail/pose_array__functions.h"

bool
lhd_msgs__srv__GetWaypoints_Response__init(lhd_msgs__srv__GetWaypoints_Response * msg)
{
  if (!msg) {
    return false;
  }
  // waypoints
  if (!geometry_msgs__msg__PoseArray__init(&msg->waypoints)) {
    lhd_msgs__srv__GetWaypoints_Response__fini(msg);
    return false;
  }
  // success
  return true;
}

void
lhd_msgs__srv__GetWaypoints_Response__fini(lhd_msgs__srv__GetWaypoints_Response * msg)
{
  if (!msg) {
    return;
  }
  // waypoints
  geometry_msgs__msg__PoseArray__fini(&msg->waypoints);
  // success
}

bool
lhd_msgs__srv__GetWaypoints_Response__are_equal(const lhd_msgs__srv__GetWaypoints_Response * lhs, const lhd_msgs__srv__GetWaypoints_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // waypoints
  if (!geometry_msgs__msg__PoseArray__are_equal(
      &(lhs->waypoints), &(rhs->waypoints)))
  {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
lhd_msgs__srv__GetWaypoints_Response__copy(
  const lhd_msgs__srv__GetWaypoints_Response * input,
  lhd_msgs__srv__GetWaypoints_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // waypoints
  if (!geometry_msgs__msg__PoseArray__copy(
      &(input->waypoints), &(output->waypoints)))
  {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

lhd_msgs__srv__GetWaypoints_Response *
lhd_msgs__srv__GetWaypoints_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lhd_msgs__srv__GetWaypoints_Response * msg = (lhd_msgs__srv__GetWaypoints_Response *)allocator.allocate(sizeof(lhd_msgs__srv__GetWaypoints_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(lhd_msgs__srv__GetWaypoints_Response));
  bool success = lhd_msgs__srv__GetWaypoints_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
lhd_msgs__srv__GetWaypoints_Response__destroy(lhd_msgs__srv__GetWaypoints_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    lhd_msgs__srv__GetWaypoints_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
lhd_msgs__srv__GetWaypoints_Response__Sequence__init(lhd_msgs__srv__GetWaypoints_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lhd_msgs__srv__GetWaypoints_Response * data = NULL;

  if (size) {
    data = (lhd_msgs__srv__GetWaypoints_Response *)allocator.zero_allocate(size, sizeof(lhd_msgs__srv__GetWaypoints_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = lhd_msgs__srv__GetWaypoints_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        lhd_msgs__srv__GetWaypoints_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
lhd_msgs__srv__GetWaypoints_Response__Sequence__fini(lhd_msgs__srv__GetWaypoints_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      lhd_msgs__srv__GetWaypoints_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

lhd_msgs__srv__GetWaypoints_Response__Sequence *
lhd_msgs__srv__GetWaypoints_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lhd_msgs__srv__GetWaypoints_Response__Sequence * array = (lhd_msgs__srv__GetWaypoints_Response__Sequence *)allocator.allocate(sizeof(lhd_msgs__srv__GetWaypoints_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = lhd_msgs__srv__GetWaypoints_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
lhd_msgs__srv__GetWaypoints_Response__Sequence__destroy(lhd_msgs__srv__GetWaypoints_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    lhd_msgs__srv__GetWaypoints_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
lhd_msgs__srv__GetWaypoints_Response__Sequence__are_equal(const lhd_msgs__srv__GetWaypoints_Response__Sequence * lhs, const lhd_msgs__srv__GetWaypoints_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!lhd_msgs__srv__GetWaypoints_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
lhd_msgs__srv__GetWaypoints_Response__Sequence__copy(
  const lhd_msgs__srv__GetWaypoints_Response__Sequence * input,
  lhd_msgs__srv__GetWaypoints_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(lhd_msgs__srv__GetWaypoints_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    lhd_msgs__srv__GetWaypoints_Response * data =
      (lhd_msgs__srv__GetWaypoints_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!lhd_msgs__srv__GetWaypoints_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          lhd_msgs__srv__GetWaypoints_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!lhd_msgs__srv__GetWaypoints_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
