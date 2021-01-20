cmake_minimum_required(VERSION 3.19.3) # version can be different

project(my_cpp_project) #name of your project

add_subdirectory(Range/gtest/googletest) # add googletest subdirectory

include_directories(googletest/include) # this is so we can #include <gtest/gtest.h>

add_executable(TestRange Range/gtest/TestRange.cpp) # add this executable

target_link_libraries(TestRange PRIVATE gtest) # link google test to this executable