

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        
        @cache
        def dfs(left, right, kk):
            # 区间缩小到空或单字符，一定是回文
            if left >= right:
                return True
            # 无删除次数且首尾不同，无法形成回文
            if s[left] != s[right] and kk <= 0:
                return False
            # 首尾相同，缩小区间
            if s[left] == s[right]:
                return dfs(left + 1, right - 1, kk)
            # 首尾不同，尝试删除左端或右端
            return dfs(left + 1, right, kk - 1) or dfs(left, right - 1, kk - 1)
        
        return dfs(0, n - 1, k)