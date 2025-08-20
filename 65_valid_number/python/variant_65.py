class Solution(object):
    def isNumber(self, s: str):
        seen_digit = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in "+-":
                if i != 0:
                    return False
            elif c == '.':
                if seen_dot:
                    return False
                seen_dot = True
            else:
                return False
        
        return seen_digit


if __name__ == "__main__":
    solution = Solution()
    assert solution.isNumber("0089")
    assert solution.isNumber("-0.1")
    assert solution.isNumber("+3.14")
    assert solution.isNumber("4.")
    assert solution.isNumber("-.9")
    assert solution.isNumber("420")
    assert solution.isNumber("+3")
    assert solution.isNumber("-10")
    assert solution.isNumber("2")
    # Exponents not valid anymore
    assert not solution.isNumber("3e+7")
    assert not solution.isNumber("+6e-1")
    assert not solution.isNumber("53.5e93")
    assert not solution.isNumber("-123.456e789")
    assert not solution.isNumber("abc")
    assert not solution.isNumber("2e10")
    assert not solution.isNumber("-90E3")
    assert not solution.isNumber("1a")
    assert not solution.isNumber("1e")
    assert not solution.isNumber("e3")
    assert not solution.isNumber("99e2.5")
    assert not solution.isNumber("--6")
    assert not solution.isNumber("-+3")
    assert not solution.isNumber("95a54e53")
    assert not solution.isNumber("7..")
    assert not solution.isNumber(".")
    assert not solution.isNumber("3-")
    assert not solution.isNumber("+7e5")
    assert not solution.isNumber("7E5")
    assert not solution.isNumber("7ee")
    assert not solution.isNumber("7e")
    assert not solution.isNumber("8e1.2")
    assert not solution.isNumber("+20e-5")
    assert not solution.isNumber("Abc")
