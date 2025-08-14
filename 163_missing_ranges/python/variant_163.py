class Solution:
    def findMissingRangesVariant(self, nums, lower, upper):
        nums = [lower - 1] + nums + [upper + 1]
        prev = nums[0]
        res = []
        
        for cur in nums[1:]:
            # 计算缺失数字的数量：cur - prev - 1（prev和cur之间的数字个数）
            missing_count = cur - prev - 1
            
            if missing_count > 2:
                # 缺失>2个：用区间表示
                res.append(f"{prev + 1}-{cur - 1}")
            elif missing_count == 2:
                # 缺失正好2个：分别添加两个数字
                res.append(str(prev + 1))
                res.append(str(prev + 2))
            elif missing_count == 1:
                # 缺失1个：添加单个数字
                res.append(str(prev + 1))
            
            prev = cur
        return res

if __name__ == "__main__":
    solution = Solution()
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    solution = Solution()
    # Empty vector cases
    assert solution.findMissingRangesVariant([], 0, 0) == ["0"]
    assert solution.findMissingRangesVariant([], 5, 35) == ["5-35"]
    assert solution.findMissingRangesVariant([], 0, 35) == ["0-35"]

    # Valid cases
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 2, 87) == [
        "2-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-87",
    ]

    # Upper bound with dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 800) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21-800",
    ]

    # Upper bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 21) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
    ]

    # Upper bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 22) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # Upper bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 1, 20) == [
        "1-4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # No missing ranges with one element
    assert solution.findMissingRangesVariant([0], 0, 0) == []

    # No missing ranges with one element V2
    assert solution.findMissingRangesVariant([6], 6, 6) == []

    # Lower bound with dash
    assert solution.findMissingRangesVariant([0, 8, 9, 15, 16, 18, 20], 0, 20) == [
        "1-7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with no missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 20) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with two missing numbers
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 3, 20) == [
        "3",
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Lower bound with one missing number
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 4, 20) == [
        "4",
        "6",
        "7",
        "10-14",
        "17",
        "19",
    ]

    # Upper bound with no dash
    assert solution.findMissingRangesVariant([5, 8, 9, 15, 16, 18, 20], 5, 22) == [
        "6",
        "7",
        "10-14",
        "17",
        "19",
        "21",
        "22",
    ]

    # One element with two ranges missing
    assert solution.findMissingRangesVariant([10], 5, 22) == ["5-9", "11-22"]
