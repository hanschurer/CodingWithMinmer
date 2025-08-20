class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        res = 0
        sign = 1
        int_max, int_min = 2**31-1, -2**31
        if not s: return 0
        if s[0] in ["+","-"]:
            sign = -1 if s[0] == "-" else 1
            s = s[1:]
        for c in s:
            if c.isdigit():
                res=  res*10 + int(c)
            else:
                break
        
        res*= sign
        if res>= int_max:
            return int_max
        if res <= int_min:
            return int_min
        return res
        