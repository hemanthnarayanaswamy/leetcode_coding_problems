class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        result = 0

        for x, y in dominoes:
            if x > y: x, y = y, x

            val = x * 10 + y

            result += num[val]
            num[val] += 1
        
        return result
        