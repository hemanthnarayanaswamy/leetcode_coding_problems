class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count = 0 
        freq = defaultdict(list)

        for i, num in enumerate(nums):
            freq[num].append(i)
        
        for arr in freq.values():
            n = len(arr)
            if max(arr) - min(arr) + 1 == n:
                count += 1
        
        return count
                

        
            
