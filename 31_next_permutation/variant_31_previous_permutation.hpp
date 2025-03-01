#pragma once

#include <vector>

// VARIANT: What if you had to find the previous permutation?
void prevPermutation_31(std::vector<int>& nums) {
    int peak = -1;
    for (int i = nums.size() - 2; i >= 0; i--) {
        int num = nums[i];
        int num_after = nums[i + 1];

        if (num > num_after) {
            peak = i;
            break;
        }
    }
    if (peak == -1) {
        std::reverse(nums.begin(), nums.end());
        return;
    }

    int next_lower = nums.size() - 1;
    while (nums[next_lower] >= nums[peak])
        next_lower--;

    std::swap(nums[peak], nums[next_lower]);
    std::reverse(nums.begin() + peak + 1, nums.end());
}
