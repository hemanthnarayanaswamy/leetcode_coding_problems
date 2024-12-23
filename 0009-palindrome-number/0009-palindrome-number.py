class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False

        reverse = 0
        temp = x

        while (temp != 0):
            remainder = temp % 10
            reverse = reverse * 10 + remainder 
            temp = temp / 10 
        
        return True if reverse == x else False

## You can use Strings to do it easily 
""" 
value = str(x) # convert it into string and reverse the string
        if value == value[::-1]:
            return True
        return False
"""
