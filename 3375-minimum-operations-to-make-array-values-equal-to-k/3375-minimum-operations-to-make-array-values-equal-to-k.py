class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        freq = dict(sorted(Counter(nums).items(), reverse=True))
        
        if min(freq) < k:
            return -1
        
        operations = 0 
        for key in freq:
            if key != k:
                operations += 1
            else:
                break
        
        return operations
