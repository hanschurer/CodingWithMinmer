class Solution:
    def calculate(self, s: str) -> int:
        cur = pre = res = 0
        op = "+"
        s = s.strip()

        for i, v in enumerate(s):
            if v.isdigit():
                cur = cur * 10 + int(v)
            if i == len(s)-1 or v in "+-*/":
                if op == "+":
                    res +=pre
                    pre = cur
                elif op =="-":
                    res+=pre
                    pre = -cur
                elif op =="*":
                    pre = pre*cur
                elif op =="/":
                    pre = int(pre / cur)
                cur  = 0
                op = v
        
        return res+pre