class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half_len = len(nums)//2
        result = []
        
        for i,j in zip(range(0, n),range(n, 2*n)):
            result.append(nums[i])
            result.append(nums[j])
        
        return result

        