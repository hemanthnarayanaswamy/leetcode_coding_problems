class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000} ## Decalare the roman representation to refer and compute the value from

        result = 0 ## Value to store the result

        for index in range(len(s)): #3 Looping through the elements in the string
            if index + 1 < len(s) and roman[s[index]] < roman[s[index + 1]]:
                # 1. Check if the next index is not out of range 
                # 2. check if its ascending or descending value 
                result -= roman[s[index]]
            else:
                result += roman[s[index]]
        return result

## Fastest result code 
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }

        total = 0
        prev = 0

        for i in reversed(s):
            cur = value_map[i]
            if cur < prev:
                total -= cur
            else:
                total += cur
            prev = cur

        return total
