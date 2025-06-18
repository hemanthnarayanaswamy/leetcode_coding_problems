class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = {}
        result = []
        n = len(nums)

        for i in range(n):
            for j in range(len(nums[i])):
                counter[nums[i][j]] = counter.get(nums[i][j], 0) + 1
        
        for num, freq in counter.items():
            if freq == n:
                result.append(num)

        return sorted(result)
