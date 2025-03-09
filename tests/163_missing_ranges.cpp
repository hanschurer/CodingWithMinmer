#include <gtest/gtest.h>
#include "../163_missing_ranges/variant_163.hpp"

// Length can be empty
TEST(MissingRanges_Variant, EmptyVectorOnly0) {
    std::vector<int> nums = {};
    int lower = 0, upper = 0;
    std::vector<std::string> expected = {"0"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, EmptyVectorOneBigMissingRange) {
    std::vector<int> nums = {};
    int lower = 5, upper = 35;
    std::vector<std::string> expected = {"5-35"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, EmptyVectorLowerBoundZero) {
    std::vector<int> nums = {};
    int lower = 0, upper = 35;
    std::vector<std::string> expected = {"0-35"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}

TEST(MissingRanges_Variant, Valid) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 2, upper = 87;
    std::vector<std::string> expected = {"2-4", "6", "7", "10-14", "17", "19", "21-87"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_UpperBoundDash) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 1, upper = 800;
    std::vector<std::string> expected = {"1-4", "6", "7", "10-14", "17", "19", "21-800"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_UpperBoundOneMissing) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 1, upper = 21;
    std::vector<std::string> expected = {"1-4", "6", "7", "10-14", "17", "19", "21"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_UpperBoundTwoMissing) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 1, upper = 22;
    std::vector<std::string> expected = {"1-4", "6", "7", "10-14", "17", "19", "21", "22"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_UpperBoundNoneMissing) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 1, upper = 20;
    std::vector<std::string> expected = {"1-4", "6", "7", "10-14", "17", "19"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_NoMissingRangesWithOneElement) {
    std::vector<int> nums = {0};
    int lower = 0, upper = 0;
    EXPECT_EQ(std::vector<std::string>(), findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_NoMissingRangesWithOneElementV2) {
    std::vector<int> nums = {6};
    int lower = 6, upper = 6;
    EXPECT_EQ(std::vector<std::string>(), findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_LowerBoundDash) {
    std::vector<int> nums = {0, 8, 9, 15, 16, 18, 20};
    int lower = 0, upper = 20;
    std::vector<std::string> expected = {"1-7", "10-14", "17", "19"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_LowerBoundNoMissing) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 5, upper = 20;
    std::vector<std::string> expected = {"6", "7", "10-14", "17", "19"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRangesVariant, Valid_LowerBoundTwoMissing) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 3, upper = 20;
    std::vector<std::string> expected = {"3", "4", "6", "7", "10-14", "17", "19"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_LowerBoundOneMissing) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 4, upper = 20;
    std::vector<std::string> expected = {"4", "6", "7", "10-14", "17", "19"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_UpperBoundNoDash) {
    std::vector<int> nums = {5, 8, 9, 15, 16, 18, 20};
    int lower = 5, upper = 22;
    std::vector<std::string> expected = {"6", "7", "10-14", "17", "19", "21", "22"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}
TEST(MissingRanges_Variant, Valid_OneElementTwoRanges) {
    std::vector<int> nums = {10};
    int lower = 5, upper = 22;
    std::vector<std::string> expected = {"5-9", "11-22"};
    EXPECT_EQ(expected, findMissingRanges_variant_163(nums, lower, upper));
}