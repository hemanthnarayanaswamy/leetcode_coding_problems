class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        result = 0

        for i in range(len(num_str)-k+1):
            temp = int(num_str[i:i+k])
            if temp != 0 and num % temp == 0:
                result += 1
        return result
        