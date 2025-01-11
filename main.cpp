#include "1249_minimum_remove_to_make_valid_parentheses/mock_interview_1249.hpp"
#include "1249_minimum_remove_to_make_valid_parentheses/first_variant_in_place_1249.hpp"
#include "1249_minimum_remove_to_make_valid_parentheses/original_1249.hpp"
#include "125_valid_palindrome/variant_125.hpp"
#include "1650_lowest_common_ancestor_3/second_variant_input_vector_1650.hpp"
#include "199_binary_tree_right_side_view/first_variant_left_right_side_views_199.hpp"
#include "199_binary_tree_right_side_view/second_variant_print_left_right_side_views_199.hpp"
#include "283_move_zeroes/variant_zeroes_to_front_283.hpp"
#include "528_random_pick_weight/first_variant_country_population_528.hpp"
#include "71_simplify_path/first_variant_cwd_cd_71.hpp"
#include "88_merged_sorted_array/variant_without_sizes_88.hpp"
#include "938_range_of_sum_bst/first_variant_average_938.hpp"
#include "938_range_of_sum_bst/second_variant_many_invocations_938.hpp"
#include "1570_dot_product_of_two_sparse_vectors/original_1570.hpp"
#include "1570_dot_product_of_two_sparse_vectors/variant_binary_search_1570.hpp"
#include "1762_buildings_with_an_ocean_view/first_variant_view_count_1762.hpp"
#include "1762_buildings_with_an_ocean_view/second_variant_ocean_view_both_sides_1762.hpp"
#include "346_moving_average_from_data_stream/variant_sliding_window_346.hpp"
#include "1004_max_consecutive_ones_3/first_variant_1004.hpp"
#include "1004_max_consecutive_ones_3/second_variant_1004.hpp"

int main(int argc, char *argv[]) {
    if (!strcmp(argv[1], "1249_minimum_remove_to_make_valid_parentheses")) {
        delete_least_parentheses();
    }
    else if (!strcmp(argv[1], "71_simplify_path")) {
        change_directory();
    }
    else if (!strcmp(argv[1], "938_range_sum_of_bst")) {
        range_sum_calculator();
        // average_of_bst();
    }
    else if (!strcmp(argv[1], "283_move_zeroes")) {
        move_zeroes_to_front();
    }
    else if (!strcmp(argv[1], "199_binary_tree_right_side_view")) {
        // get_left_right_side_views();
        print_left_right_side_views();
    }
    else if (!strcmp(argv[1], "1650_lowest_common_ancestor_3")) {
        lowestCommonAncestor_second_variant_1650();
    }
    else if (!strcmp(argv[1], "528_random_pick_with_weight")) {
        pickIndex();
    }
    else if (!strcmp(argv[1], "88_merge_sorted_array")) {
        merge_vectors_88();
    }
    else if (!strcmp(argv[1], "1570_dot_product_of_two_sparse_vectors")) {
        dotProductVariant();
    }
    else if (!strcmp(argv[1], "1762_buildings_with_an_ocean_view")) {
        findBuildingViewCount_second_variant_1762();
    }
    else if (!strcmp(argv[1], "125_valid_palindrome")) {
        isPalindrome_variant_125();
    }
    else if (!strcmp(argv[1], "346_moving_average_from_data_stream")) {
        compute_running_sum_variant_346();
    }
    else if (!strcmp(argv[1], "1004_max_consecutive_ones_3")) {
        longestVacationTimeSecondVariant();
    }
}

