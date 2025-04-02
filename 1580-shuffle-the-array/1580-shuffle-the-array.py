class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half_len = len(nums)//2
        result = [0] * 2 * n
        current = 0
        
        for i,j in zip(range(0, n),range(n, 2*n)):
            result[current] = nums[i]
            current += 1
            result[current] = nums[j]
            current += 1
        
        return result

        