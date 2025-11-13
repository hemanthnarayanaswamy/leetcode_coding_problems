class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        onesCounter = 0
        shift = False

        for i in range(len(s)-1):
            if s[i] == '1':
                onesCounter += 1
            else:
                if s[i+1] == '1':
                    operations += onesCounter 

        if s[-1] == '0':
            operations += onesCounter      
        
        return operations