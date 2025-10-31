class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == 2:
                res.append(num)
            
            if len(res) == 2:
                return res