class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        numsSort = sorted(nums, reverse=True)
        
        return max(numsSort[-1]* numsSort[-2]* numsSort[0], numsSort[0]*numsSort[1]*numsSort[2])

        
       
        