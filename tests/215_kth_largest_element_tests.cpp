#include <gtest/gtest.h>
#include "../215_kth_largest_element/second_variant_kth_smallest_215.hpp"
#include "../215_kth_largest_element/first_variant_kth_largest_215.hpp"

TEST(findKthSmallest_FirstVariant, DistinctElements) {
    std::vector<int> nums = {3, 8, 4, 1, 10};
    int k = 1;
    EXPECT_EQ(1, findKthSmallest_215(nums, k));
    k = 2;
    EXPECT_EQ(3, findKthSmallest_215(nums, k));
    k = 3;
    EXPECT_EQ(4, findKthSmallest_215(nums, k));
    k = 4;
    EXPECT_EQ(8, findKthSmallest_215(nums, k));
    k = 5;
    EXPECT_EQ(10, findKthSmallest_215(nums, k));
}
TEST(findKthSmallest_FirstVariant, DuplicateElements) {
    std::vector<int> nums = {1, 1, 1, 1, 2};
    int k = 1;
    EXPECT_EQ(1, findKthSmallest_215(nums, k));
    k = 2;
    EXPECT_EQ(1, findKthSmallest_215(nums, k));
    k = 3;
    EXPECT_EQ(1, findKthSmallest_215(nums, k));
    k = 4;
    EXPECT_EQ(1, findKthSmallest_215(nums, k));
    k = 5;
    EXPECT_EQ(2, findKthSmallest_215(nums, k));
}
TEST(findKthSmallest_FirstVariant, NegativeElements) {
    std::vector<int> nums = {-1, -5, -2, -3, -4};
    int k = 1;
    EXPECT_EQ(-5, findKthSmallest_215(nums, k));
    k = 2;
    EXPECT_EQ(-4, findKthSmallest_215(nums, k));
    k = 3;
    EXPECT_EQ(-3, findKthSmallest_215(nums, k));
    k = 4;
    EXPECT_EQ(-2, findKthSmallest_215(nums, k));
    k = 5;
    EXPECT_EQ(-1, findKthSmallest_215(nums, k));
}

TEST(findKthPlusOne_SecondVariant_LargestVariant, DistinctElements) {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    int k = 0;
    EXPECT_EQ(5, findKthLargest_first_variant_215(nums, k));
    k = 1;
    EXPECT_EQ(4, findKthLargest_first_variant_215(nums, k));
    k = 2;
    EXPECT_EQ(3, findKthLargest_first_variant_215(nums, k));
    k = 3;
    EXPECT_EQ(2, findKthLargest_first_variant_215(nums, k));
    k = 4;
    EXPECT_EQ(1, findKthLargest_first_variant_215(nums, k));

    nums = {1};
    k = 0;
    EXPECT_EQ(1, findKthLargest_first_variant_215(nums, k));
}
TEST(findKthPlusOne_SecondVariant_LargestVariant, OutOfRange) {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    EXPECT_THROW(findKthLargest_first_variant_215(nums, 5), std::out_of_range);
    EXPECT_THROW(findKthLargest_first_variant_215(nums, 50), std::out_of_range);

    nums = {1};
    int k = 1;
    EXPECT_THROW(findKthLargest_first_variant_215(nums, k), std::out_of_range);

    nums = {}; // Empty vector?
    k = 0;
    EXPECT_THROW(findKthLargest_first_variant_215(nums, k), std::out_of_range);
    k = 1;
    EXPECT_THROW(findKthLargest_first_variant_215(nums, k), std::out_of_range);
    k = 2;
    EXPECT_THROW(findKthLargest_first_variant_215(nums, k), std::out_of_range);
}