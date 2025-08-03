class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if counts.get(nums[i + 1]):
                    counts[nums[i + 1]] += 1
                else:
                    counts[nums[i + 1]] = 1
        return max(counts, key=counts.get)