class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        chosen_num = max(nums)
        k_operation = chosen_num + k - 1

        maxSum = (k_operation*(k_operation + 1)) - (chosen_num*(chosen_num -1))
        return maxSum // 2