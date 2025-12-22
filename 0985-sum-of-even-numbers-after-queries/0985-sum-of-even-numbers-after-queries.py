class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = sum(x for x in nums if x % 2 == 0)
        answer = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even += nums[idx]

            answer.append(even)
        return answer