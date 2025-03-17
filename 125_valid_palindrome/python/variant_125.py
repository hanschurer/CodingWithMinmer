class Solution:
    def isPalindrome(self, s: str, include: list[str]) -> bool:
        include_set = set(include)
        left, right = 0, len(s) - 1
        while left < right:
            while s[left] not in include_set and left < right:
                left += 1
            while s[right] not in include_set and left < right:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    assert not solution.isPalindrome("racecarX", ["r", "X"])
    assert solution.isPalindrome("Yo, banana boY!", ["Y", "o", "b", "a", "n"])
    assert solution.isPalindrome("yo banana boy!", ["y", "o", "b", "a", "n"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", " ", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "c", "d", "e"])
    assert solution.isPalindrome("a b c d e d c b a", ["a", "b", "e"])
    assert not solution.isPalindrome("Wow", ["W", "o", "w"])
    assert solution.isPalindrome("WwoWWWWWWWWWWWWWow", ["o", "w"])
    assert solution.isPalindrome("__________________", ["1", "2"])
    assert not solution.isPalindrome("________133__________", ["1", "3"])
    assert not solution.isPalindrome("____1____133_______________", ["1", "3", "_"])
    assert solution.isPalindrome("", ["1", "3", "_"])
    assert solution.isPalindrome("", [])
    assert solution.isPalindrome("MadaM", [])
    assert solution.isPalindrome("MadaM", ["z", "M", "d"])
    assert not solution.isPalindrome("MadaMM", ["z", "M", "d"])
    assert not solution.isPalindrome("racecarX", ["r", "X"])
