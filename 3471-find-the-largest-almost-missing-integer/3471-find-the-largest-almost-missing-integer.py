from collections import Counter 

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        nums_freq = Counter(nums)
        n = len(nums)

        if k == 1:
            res = -1
            for key, val in nums_freq.items():
                if val == 1 and key > res:
                    res = key
            return res

        elif k == n:
            return max(nums)

        elif 1 < k < n:
            count_first = nums_freq[nums[0]]
            count_last = nums_freq[nums[-1]]
            if count_first > 1 and count_last > 1:
                return -1
            else:
                if count_first > 1 and count_last == 1:
                    return nums[-1]
                elif count_first == 1 and count_last > 1:
                    return nums[0]
                else:
                    return max(nums[0], nums[-1])