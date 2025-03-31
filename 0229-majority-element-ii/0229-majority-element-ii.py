class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        major_condition = len(nums) // 3
        result = []
        nums_freq = Counter(nums)

        for key, value in nums_freq.items():
            if value > major_condition:
                result.append(key)

        return result