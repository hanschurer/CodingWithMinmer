

class Solution:
    def minimumAddToMakeValid(self, s: str) -> str:
        res = []
        l = 0
        for c in s:
            if c == "(":
                l +=1
            elif c == ")":
                if l > 0:
                    l-=1
                else:
                    res.append("(")
            res.append(c)
        
        res += [")"] * l
        return "".join(res)
                
if __name__ == "__main__":
    solution = Solution()
    assert solution.minimumAddToMakeValid("(())((") == "(())(())"
    assert solution.minimumAddToMakeValid("))(") == "()()()"
    assert solution.minimumAddToMakeValid(")))") == "()()()"
    assert solution.minimumAddToMakeValid("(((") == "((()))"
    assert solution.minimumAddToMakeValid("") == ""
    assert solution.minimumAddToMakeValid("(())") == "(())"
    assert solution.minimumAddToMakeValid(")))(((") == "()()()((()))"
    assert solution.minimumAddToMakeValid("abcxyz") == "abcxyz"
    assert solution.minimumAddToMakeValid("(()()))((") == "(()())()(())"
    assert solution.minimumAddToMakeValid("((a)()))((xyz") == "((a)())()((xyz))"