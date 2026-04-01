class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = tmp = 0

        for num in freq:
            if freq[num+1]:
                tmp = freq[num] + freq[num+1]

            if tmp and tmp > res:
                res = tmp
        
        return res