class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = tmp = 0

        for key, count in freq.items():
            if freq[key+1]:
                tmp = count + freq.get(key+1, 0)

            if tmp and tmp > res:
                res = tmp
        
        return res