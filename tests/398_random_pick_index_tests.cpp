#pragma once

#include <gtest/gtest.h>
#include <unordered_set>
#include "../398_random_pick_index/first_variant_398.hpp"
#include "../398_random_pick_index/second_variant_398.hpp"

TEST(RandomPickIndex_FirstVariant_SampleK, HappyCase) {
    std::vector<int> nums = {6, 8, 2, 1, 3, 10, 4};
    int k = 3;
    std::unordered_set<int> expected_nums(nums.begin(), nums.end());
    for (int i = 0; i < 1000; i++) {
        std::vector<int> actual = randomPickIndices_first_variant_398(nums, k);
        EXPECT_EQ(3, actual.size());
        EXPECT_TRUE(expected_nums.contains(actual[0]));
        EXPECT_TRUE(expected_nums.contains(actual[1]));
        EXPECT_TRUE(expected_nums.contains(actual[2]));
    }
}
TEST(RandomPickIndex_FirstVariant_SampleK, NegativeNumbers) {
    std::vector<int> nums = {6, -1, 8, 2, 100, 3, 10, -3, -50, 4};
    int k = 4;
    std::unordered_set<int> expected_nums(nums.begin(), nums.end());
    for (int i = 0; i < 1000; i++) {
        std::vector<int> actual = randomPickIndices_first_variant_398(nums, k);
        EXPECT_EQ(4, actual.size());
        EXPECT_TRUE(expected_nums.contains(actual[0]));
        EXPECT_TRUE(expected_nums.contains(actual[1]));
        EXPECT_TRUE(expected_nums.contains(actual[2]));
        EXPECT_TRUE(expected_nums.contains(actual[3]));
    }
}
TEST(RandomPickIndex_FirstVariant_SampleK, K_Equals_N) {
    std::vector<int> nums = {6, -1, 8, 2, 100, 3, 10, -3, -50, 4};
    int k = 10;
    for (int i = 0; i < 1000; i++) {
        std::vector<int> actual = randomPickIndices_first_variant_398(nums, k);
        EXPECT_EQ(10, actual.size());
        EXPECT_EQ(6, actual[0]);
        EXPECT_EQ(-1, actual[1]);
        EXPECT_EQ(8, actual[2]);
        EXPECT_EQ(2, actual[3]);
        EXPECT_EQ(100, actual[4]);
        EXPECT_EQ(3, actual[5]);
        EXPECT_EQ(10, actual[6]);
        EXPECT_EQ(-3, actual[7]);
        EXPECT_EQ(-50, actual[8]);
        EXPECT_EQ(4, actual[9]);
    }
}
////////////////////////////////////////////////////////////////////////
TEST(RandomPickIndex_SecondVariant_SampleIndexOfMaxNum, HappyCase) {
    std::vector<int> nums = {11, 11, 2, 30, 6, 30, 30, 2, 62, 62};
    std::unordered_set<int> expected_indices{8, 9};
    for (int i = 0; i < 1000; i++) {
        int picked_index = randomPickIndex_second_variant_398(nums);
        EXPECT_TRUE(expected_indices.contains(picked_index));
        EXPECT_EQ(62, nums[picked_index]);
    }
}
TEST(RandomPickIndex_SecondVariant_SampleIndexOfMaxNum, NegativeNumbers) {
    std::vector<int> nums = {11, 11, 2, 30, 6, 30, 30, 2, 62, 62, -1, -2, -3, -4};
    std::unordered_set<int> expected_indices{8, 9};
    for (int i = 0; i < 1000; i++) {
        int picked_index = randomPickIndex_second_variant_398(nums);
        EXPECT_TRUE(expected_indices.contains(picked_index));
        EXPECT_EQ(62, nums[picked_index]);
    }
}
TEST(RandomPickIndex_SecondVariant_SampleIndexOfMaxNum, AllDuplicates) {
    std::vector<int> nums = {1, 1, 1, 1, 1};
    std::unordered_set<int> expected_indices{0, 1, 2, 3, 4};
    for (int i = 0; i < 1000; i++) {
        int picked_index = randomPickIndex_second_variant_398(nums);
        EXPECT_TRUE(expected_indices.contains(picked_index));
        EXPECT_EQ(1, nums[picked_index]);
    }
}
TEST(RandomPickIndex_SecondVariant_SampleIndexOfMaxNum, OneElement) {
    std::vector<int> nums = {9000};
    std::unordered_set<int> expected_indices{0};
    for (int i = 0; i < 1000; i++) {
        int picked_index = randomPickIndex_second_variant_398(nums);
        EXPECT_TRUE(expected_indices.contains(picked_index));
        EXPECT_EQ(9000, nums[picked_index]);
    }
}