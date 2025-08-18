class Solution_227_Variant:
    def calculate(self, s: str) -> int:
        curr_num = 0
        prev_num = 0
        result = 0
        op = '+'
        
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
        
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if op == '+':
                    result += prev_num
                    prev_num = curr_num
                elif op == '*':
                    prev_num = prev_num * curr_num
        
                curr_num = 0
                op = s[i]
        
        result += prev_num
        return result
