# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_lhd_mapping_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED lhd_mapping_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(lhd_mapping_FOUND FALSE)
  elseif(NOT lhd_mapping_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(lhd_mapping_FOUND FALSE)
  endif()
  return()
endif()
set(_lhd_mapping_CONFIG_INCLUDED TRUE)

# output package information
if(NOT lhd_mapping_FIND_QUIETLY)
  message(STATUS "Found lhd_mapping: 0.0.0 (${lhd_mapping_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'lhd_mapping' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${lhd_mapping_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(lhd_mapping_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${lhd_mapping_DIR}/${_extra}")
endforeach()
