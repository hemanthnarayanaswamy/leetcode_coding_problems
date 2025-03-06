class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = []
        temp_sum, final_sum = 0, 0
        
        for char in s:
            result.append(str(ord(char)-96))
        
        result = ''.join(result)

        while k > 0:
            temp_sum = sum([int(i) for i in result])
            final_sum = temp_sum
            result = str(temp_sum)
            temp_sum = 0
            k -= 1
        return final_sum
        