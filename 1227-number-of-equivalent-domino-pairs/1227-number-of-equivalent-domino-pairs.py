class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = {}
        result = 0

        for x, y in dominoes:
            if x > y: x, y = y, x
            val = x * 10 + y
            count = num.get(val, 0)
            result += count
            num[val] = count + 1
        
        return result
        