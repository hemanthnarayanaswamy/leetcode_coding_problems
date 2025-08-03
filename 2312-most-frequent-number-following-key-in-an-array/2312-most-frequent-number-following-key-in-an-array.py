class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = {}
        for a, b in zip(nums, nums[1:]):
            if a == key:
                freq[b] = freq.get(b, 0) + 1
        
        return max(freq, key=freq.get)