#include <gtest/gtest.h>
#include "../34_find_first_and_last_position_of_element_in_array/first_variant_34.hpp"
#include "../34_find_first_and_last_position_of_element_in_array/second_variant_34.hpp"

TEST(FindFirstLastPositionOfElement_FirstVariant, Valid) {
    std::vector<int> nums = {5, 7, 7, 8, 8, 10};
    int target = 8;
    EXPECT_EQ(2, searchRange_first_variant_34(nums, target));
    target = 6;
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));

    nums = {2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12};
    target = 9;
    EXPECT_EQ(5, searchRange_first_variant_34(nums, target));
    target = 2;
    EXPECT_EQ(2, searchRange_first_variant_34(nums, target));
    target = 3;
    EXPECT_EQ(3, searchRange_first_variant_34(nums, target));
    target = 10;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 12;
    EXPECT_EQ(2, searchRange_first_variant_34(nums, target));

    nums = {1, 2, 3, 4, 5};
    target = 1;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 2;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 3;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 4;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 5;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));

    nums = {1, 1, 1, 1, 1, 1, 1, 1, 1};
    target = 1;
    EXPECT_EQ(9, searchRange_first_variant_34(nums, target));

    nums = {-3, -2, -1, 0, 1, 2, 3};
    target = -3;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = -2;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = -1;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 0;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 1;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 2;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
    target = 3;
    EXPECT_EQ(1, searchRange_first_variant_34(nums, target));
}
TEST(FindFirstLastPositionOfElement_FirstVariant, TargetNotFound) {
    std::vector<int> nums = {5, 7, 7, 8, 8, 10};
    int target = 9; // Not Found
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
    target = 6; // Not Found
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
    target = -5; // Too low
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
    target = 60; // Too high
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));

    nums = {};
    target = -5; // Empty vector
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
    target = 50; // Empty vector
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));

    nums = {2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12};
    target = 1; // Too low
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
    target = 4; // Not found
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
    target = 15; // Too high
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));

    nums = {1, 2, 3, 4, 5};
    target = 0;
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
    target = 6;
    EXPECT_EQ(0, searchRange_first_variant_34(nums, target));
}
////////////////////////////////////////////////////////////////
TEST(FindFirstLastPositionOfElement_SecondVariant, NonzeroCount) {
    std::vector<int> nums = {2, 2, 3, 3, 3, 9, 9, 9, 9, 9, 10, 12, 12};
    EXPECT_EQ(5, countUniqueElements_second_variant_34(nums));

    nums = {-3, -2, -1, 0, 1, 2, 3};
    EXPECT_EQ(7, countUniqueElements_second_variant_34(nums));

    nums = {-3, -3, -3, -2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3};
    EXPECT_EQ(7, countUniqueElements_second_variant_34(nums));

    nums = {1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 7, 7, 8, 8, 10};
    EXPECT_EQ(6, countUniqueElements_second_variant_34(nums));

    nums = {19, 19, 19, 19};
    EXPECT_EQ(1, countUniqueElements_second_variant_34(nums));

    nums = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    EXPECT_EQ(1, countUniqueElements_second_variant_34(nums));

    nums = {9001};
    EXPECT_EQ(1, countUniqueElements_second_variant_34(nums));

    nums = {5, 7, 7, 8, 8, 10};
    EXPECT_EQ(4, countUniqueElements_second_variant_34(nums));

    nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    EXPECT_EQ(10, countUniqueElements_second_variant_34(nums));
}
TEST(FindFirstLastPositionOfElement_SecondVariant, ZeroCount) {
    std::vector<int> nums = {};
    EXPECT_EQ(0, countUniqueElements_second_variant_34(nums));
}