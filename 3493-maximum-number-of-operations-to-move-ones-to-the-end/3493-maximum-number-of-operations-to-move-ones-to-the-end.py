class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        onesCounter = 0
        n = len(s)

        for i, b in enumerate(s):
            if b == '1':
                onesCounter += 1
            else:
                if i == n - 1 or s[i+1] == '1':
                    operations += onesCounter 

        return operations