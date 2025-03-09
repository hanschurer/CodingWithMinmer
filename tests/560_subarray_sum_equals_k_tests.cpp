#include <gtest/gtest.h>
#include "../560_subarray_sum_equals_k/first_variant_560.hpp"
#include "../560_subarray_sum_equals_k/second_variant_560.hpp"

TEST(SubarraySum_FirstVariant, True) {
    std::vector<int> nums = {1, 1, 1};
    int k = 2;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 2, 3, 1, 1, 1};
    k = 5;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 2, 3, 1, 1, 1};
    k = 9;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {3, 4, 7, 2, -3, 1, 4, 2, 1, -14};
    k = 7;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 2, 3, -3, 1, 1};
    k = 0;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, -3, 3, -3, 3, -3};
    k = 0;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, -3, 3, -6, 8, -3, 4, 5, 6};
    k = 8;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, -3, 3, -6, 8, -3, 4, 5, 6};
    k = -1;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {5};
    k = 5;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));
    k = 10;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    nums = {-1, -2, -3, -4};
    k = -5;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));
    k = -10;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {0, 0, 0, 0, 0};
    k = 0;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {8, 3, 6, 1, -5, 10};
    k = 10;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));
}
TEST(SubarraySum_FirstVariant, False) {
    std::vector<int> nums = {1, 1, 1};
    int k = 4;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    nums = {3, 4, 7, 2, -3, 1, 4, 2, 1, -14};
    k = -10;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    nums = {-1, -2, -3, -4};
    k = -15;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));
}

TEST(SubarraySum_SecondVariant, True) {
    std::vector<int> nums = {1, 1, 1};
    int k = 2;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 2, 3};
    k = 3;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 2, 3, 1, 1, 1};
    k = 5;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 2, 3, 1, 1, 1};
    k = 9;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {5};
    k = 5;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));
    k = 10;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    nums = {23, 5, 4, 7, 2, 11};
    k = 20;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 3, 5, 23, 2};
    k = 8;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {4, 2, 5, 2, 6, 1};
    k = 9;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));

    nums = {1, 1, 1, 1, 1, 1};
    k = 1;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));
    nums = {1};
    k = 1;
    EXPECT_TRUE(subarraySum_first_variant_560(nums, k));
}
TEST(SubarraySum_SecondVariant, False) {
    std::vector<int> nums = {1, 1, 1};
    int k = 4;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    nums = {1, 2, 3, 4, 5, 6, 7};
    k = 100;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    nums = {100, 101, 102, 103};
    k = 2;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    nums = {1, 3, 5, 23, 2};
    k = 7;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));

    // Not a possible test case since k must be >0
    nums = {1, 3, 5, 23, 2};
    k = 0;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));
    nums = {1};
    k = 0;
    EXPECT_FALSE(subarraySum_first_variant_560(nums, k));
}