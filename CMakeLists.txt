cmake_minimum_required(VERSION 3.28)
project(CodingWithMinmer)

set(CMAKE_CXX_STANDARD 20)

add_executable(CodingWithMinmer main.cpp
        1249_minimum_remove_to_make_valid_parentheses/mock_interview.hpp
        1249_minimum_remove_to_make_valid_parentheses/original_problem.hpp
        1249_minimum_remove_to_make_valid_parentheses/first_variant_in_place.hpp)
