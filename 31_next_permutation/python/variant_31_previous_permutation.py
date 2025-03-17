class Solution:
    def previousPermutation(self, nums: list[int]) -> None:
        peak = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                peak = i - 1
                break

        if peak is None:
            nums.reverse()
            return

        next_lower = len(nums) - 1
        while nums[next_lower] >= nums[peak]:
            next_lower -= 1

        nums[peak], nums[next_lower] = nums[next_lower], nums[peak]

        left = peak + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    # Basic cases
    solution = Solution()
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 3, 5]
    nums = [3, 2, 1]
    solution.previousPermutation(nums)
    assert nums == [3, 1, 2]
    nums = [1, 2, 3]
    solution.previousPermutation(nums)
    assert nums == [3, 2, 1]
    nums = [9, 6, 5, 4, 3, 2]
    solution.previousPermutation(nums)
    assert nums == [9, 6, 5, 4, 2, 3]
    nums = [4, 5, 1, 1, 3, 7]
    solution.previousPermutation(nums)
    assert nums == [4, 3, 7, 5, 1, 1]
    nums = [1, 5, 8, 5, 1, 3, 4, 6, 7]
    solution.previousPermutation(nums)
    assert nums == [1, 5, 8, 4, 7, 6, 5, 3, 1]
    nums = [9, 4, 8, 3, 5, 5, 8, 9]
    solution.previousPermutation(nums)
    assert nums == [9, 4, 5, 9, 8, 8, 5, 3]

    # Single digit case
    nums = [5]
    solution.previousPermutation(nums)
    assert nums == [5]

    # Duplicate digits case
    nums = [1, 1, 1]
    solution.previousPermutation(nums)
    assert nums == [1, 1, 1]

    # Already smallest case (loops around)
    nums = [1, 2, 3, 4, 5, 6]
    solution.previousPermutation(nums)
    assert nums == [6, 5, 4, 3, 2, 1]
