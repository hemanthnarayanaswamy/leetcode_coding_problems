class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        
        diff_freq = Counter(num - i for i, num in enumerate(nums))
        
        good_pairs = sum(freq * (freq - 1) // 2 
                        for freq in diff_freq.values() 
                        if freq > 1)
        
        return total_pairs - good_pairs