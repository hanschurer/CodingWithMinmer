#include <gtest/gtest.h>
#include "../31_next_permutation/variant_31_previous_permutation.hpp"

TEST(PreviousPermutation_Variant, Valid) {
    std::vector<int> nums = {3, 2, 1};
    std::vector<int> expected = {3, 1, 2};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);

    nums = {1, 2, 3};
    expected = {3, 2, 1};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);

    nums = {9, 6, 5, 4, 3, 2};
    expected = {9, 6, 5, 4, 2, 3};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);

    nums = {4, 5, 1, 1, 3, 7};
    expected = {4, 3, 7, 5, 1, 1};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);

    nums = {1, 5, 8, 5, 1, 3, 4, 6, 7};
    expected = {1, 5, 8, 4, 7, 6, 5, 3, 1};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);

    nums = {9, 4, 8, 3, 5, 5, 8, 9};
    expected = {9, 4, 5, 9, 8, 8, 5, 3};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums); 
}

TEST(PreviousPermutation_Variant, SingleDigitReturnsItself) {
    std::vector<int> nums = {5};
    std::vector<int> expected = {5};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);
}

TEST(PreviousPermutation_Variant, DuplicateDigitsReturnsItself) {
    std::vector<int> nums = {1, 1, 1};
    std::vector<int> expected = {1, 1, 1};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);
}

TEST(PreviousPermutation_Variant, AlreadySmallestLoopsAround) {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6};
    std::vector<int> expected = {6, 5, 4, 3, 2, 1};
    prevPermutation_31(nums);
    EXPECT_EQ(expected, nums);
}