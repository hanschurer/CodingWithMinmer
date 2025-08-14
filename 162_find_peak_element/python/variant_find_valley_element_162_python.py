#找谷底元素
def findValleyElement(nums):
    left = 0
    right = len(nums) - 2
    while left <= right:
        mid = (left+right)//2

        if nums[mid ] > nums[mid+1]:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Unreachable

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    assert findValleyElement(nums) == 0  # Left pos infinity yields valley

    nums = [1, 2, 3, 5, 3, 4, 3, 1, 6]
    print(findValleyElement(nums))
    assert findValleyElement(nums) == 4 or 7

    nums = [3, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 1

    nums = [1, 2, 3, 4, 3, 2]
    assert findValleyElement(nums) == 0

    nums = [1, 2, 3, 2, 1, 0]
    assert findValleyElement(nums) == 5  # Right pos infinity yields valley

    nums = [1, 2, 3, 2, 1, 6]
    assert findValleyElement(nums) == 4