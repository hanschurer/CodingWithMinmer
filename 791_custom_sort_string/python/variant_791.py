# 能优化frqmap吗 用 list代替 
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0]*26

        for char in s:
            freq[ord(char) - ord("a")] += 1

        result = []
        for char in order:
            i = freq[char]
            if freq[i] > 0:
                result.extend([char] * freq[i])
                freq[i] = 0

        for i, f in enumerate(freq):
            if f > 0:
                result += [chr(ord("a") + i)] * f

        return "".join(result)
