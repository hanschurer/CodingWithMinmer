#include "1249_minimum_remove_to_make_valid_parentheses/mock_interview_1249.hpp"
#include "1249_minimum_remove_to_make_valid_parentheses/first_variant_in_place_1249.hpp"
#include "1249_minimum_remove_to_make_valid_parentheses/original_1249.hpp"
#include "199_binary_tree_right_side_view/first_variant_left_right_side_views_199.hpp"
#include "199_binary_tree_right_side_view/second_variant_print_left_right_side_views_199.hpp"
#include "283_move_zeroes/variant_zeroes_to_front_283.hpp"
#include "528_random_pick_weight/first_variant_country_population_528.hpp"
#include "71_simplify_path/first_variant_cwd_cd_71.hpp"
#include "938_range_of_sum_bst/first_variant_average_938.hpp"
#include "938_range_of_sum_bst/second_variant_many_invocations_938.hpp"

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
}

