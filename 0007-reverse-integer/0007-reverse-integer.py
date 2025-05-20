class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        x = abs(x)
        
        rev=0
        while(x>0):
            digit=x%10
            rev=rev*10+digit
            x=x//10

        if rev>(2**31): # need to check for only postive condition because we have converted number into positive
            return 0
        
        return rev if (temp > 0) else -rev