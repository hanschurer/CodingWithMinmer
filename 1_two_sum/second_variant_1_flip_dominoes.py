from collections import defaultdict
from typing import List, Tuple


# SECOND VARIANT: What if you had to return the number of dominoe pairs that add up to a target?

#解法： hashmap 存key frequency的形式，key可以随便编 
def second_variant_two_sum_1(dominoes: List[Tuple[int, int]], target: int) -> int:
    domino_to_freq = defaultdict(int)
    result = 0
    for a1, a2 in dominoes:
        b1 = target - a1
        b2 = target - a2
        b_key = str(b1)+str(b2)
        if b_key in domino_to_freq:
            result += domino_to_freq[b_key]

        a_key = str(a1)+str(a2)
        domino_to_freq[a_key] +=+ 1

    return result


def test_second_variant_two_sum_1():
    dominos = [
        (3, 4),
        (1, 9),
        (3, 4),
        (2, 1),
        (9, 1),
        (9, 1),
        (7, 6),
        (1, 9)
    ]
    target = 10
    assert 6 == second_variant_two_sum_1(dominos, target)

    dominos = [  # Only digits 0-9 are permitted but these are just examples
        (1, 8),
        (12, 5),
        (12, 5),
        (12, 5),
    ]
    target = 13
    assert 3 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (1, 8),
        (12, 5),
        (12, 5),
        (12, 5),
        (1, 8)
    ]
    target = 13
    assert 6 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (1, 8),
        (12, 5),
        (12, 5),
        (12, 5),
        (1, 8),
        (12, 5),
    ]
    target = 13
    assert 8 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (1, 8),
        (1, 1),
        (5, 4),
        (1, 3),
        (1, 8),
        (12, 5),
    ]
    target = 300
    assert 0 == second_variant_two_sum_1(dominos, target)

    dominos = []
    target = 0
    assert 0 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (1, 2),
        (3, 2),
        (1, 2),
        (3, 2),
    ]
    target = 4
    assert 4 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0)
    ]
    target = 0
    assert 10 == second_variant_two_sum_1(dominos, target)

    dominos = [(3, 7)]
    target = 10
    assert 0 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (1, 9),
        (9, 1),
        (1, 9),
        (9, 1)
    ]
    target = 10
    assert 4 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    target = 10
    assert 0 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (1, 2),
        (3, 4),
        (0, 4)
    ]
    target = 1
    assert 0 == second_variant_two_sum_1(dominos, target)
   
    dominos = [
        (9, 2),
        (4, 5),
        (3, 9),
        (9, 9),
        (2, 1),
        (2, 1),
        (2, 1)
    ]
    target = 6
    assert 3 == second_variant_two_sum_1(dominos, target)

    dominos = [
        (0, 9),
        (9, 0),
        (9, 0),
        (0, 9),
        (2, 1),
        (0, 9),
        (0, 9)
    ]
    target = 9
    assert 8 == second_variant_two_sum_1(dominos, target)
    
    print("All tests passed!")


if __name__ == "__main__":
    test_second_variant_two_sum_1() 