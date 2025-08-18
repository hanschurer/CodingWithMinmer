class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1)-1,len(num2)-1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            n1 = num1[i] if i >=0 else 0
            n2 = num2[j] if j >=0 else 0

            temp = int(n1) + int(n2) + carry
            res.append(str(temp%10))
            carry = temp // 10
            i-=1
            j-=1
        res="".join(res[::-1]) 
        return "1" + res if carry else res