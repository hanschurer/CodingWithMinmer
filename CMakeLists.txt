cmake_minimum_required(VERSION 3.28)
project(CodingWithMinmer)

set(CMAKE_CXX_STANDARD 20)

add_executable(CodingWithMinmer main.cpp
        1249_minimum_remove_to_make_valid_parentheses/mock_interview_1249.hpp
        1249_minimum_remove_to_make_valid_parentheses/original_1249.hpp
        1249_minimum_remove_to_make_valid_parentheses/first_variant_in_place_1249.hpp
        71_simplify_path/first_variant_cwd_cd_71.hpp
        71_simplify_path/original_71.hpp
        938_range_of_sum_bst/second_variant_many_invocations_938.hpp
        utils/Node.hpp
        938_range_of_sum_bst/first_variant_average_938.hpp
        938_range_of_sum_bst/original_938.hpp
        283_move_zeroes/variant_zeroes_to_front_283.hpp
        283_move_zeroes/variant_zeroes_to_front_283.hpp
        283_move_zeroes/original_283.hpp
)
