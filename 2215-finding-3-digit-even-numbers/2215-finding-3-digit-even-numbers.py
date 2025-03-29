from collections import Counter 

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result= [] 
        digits_freq = Counter(digits)
        for num in range(100, 999, 2):
            temp = str(num)
            for j in temp:
                if int(j) in digits_freq:
                    if temp.count(j) > digits_freq[int(j)]:
                        break
                else:
                    break 
            else:
                result.append(num)
        return result 
        