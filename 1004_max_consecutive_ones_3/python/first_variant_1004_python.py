from typing import List

def longestOnes_first_variant_1004_python(days: List[str], pto: int) -> int:
    hashmap = {"W":0, "H":1}
    max_vacation = 0  
    left = 0
    count0 = 0
    for right in range(len(days)):
        count0 += 1 - hashmap.get(days[right])

        while count0 > pto:
            count0 -= 1 - hashmap.get( days[left])
            left += 1

        max_vacation = max(max_vacation, right - left + 1)
    return max_vacation

if __name__ == '__main__':
    days = ['W', 'H', 'H', 'W', 'W', 'H', 'W']
    pto = 2
    assert longestOnes_first_variant_1004_python(days, pto) == 5

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 0
    assert longestOnes_first_variant_1004_python(days, pto) == 2

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 5
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['W', 'W', 'H', 'H', 'W', 'W', 'W']
    pto = 10
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['H', 'H', 'H', 'H', 'H', 'H', 'H']
    pto = 0
    assert longestOnes_first_variant_1004_python(days, pto) == 7

    days = ['W', 'H', 'W', 'W', 'W', 'H', 'W', 'H']
    pto = 1
    assert longestOnes_first_variant_1004_python(days, pto) == 3
