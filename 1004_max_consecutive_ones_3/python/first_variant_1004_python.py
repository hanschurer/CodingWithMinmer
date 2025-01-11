from typing import List

def longestOnes_first_variant_1004_python(days: List[str], pto: int) -> int:
    max_vacation = 0
    left = 0
    for right in range(len(days)):
        if days[right] == 'W':
            pto -= 1

        while pto < 0:
            if days[left] == 'W':
                pto += 1
            left += 1

        max_vacation = max(max_vacation, right - left + 1)
    return max_vacation

if __name__ == '__main__':
    days = ['W', 'H', 'H', 'W', 'W', 'H', 'W']
    pto = 2
    assert longestOnes_first_variant_1004_python(days, pto) == 5
