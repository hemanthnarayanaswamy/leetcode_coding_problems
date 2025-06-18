class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n_lists = len(nums)
        counts = [0] * 1001
        # Count each distinct element per sub-array
        for arr in nums:
            # arr elements are guaranteed distinct, so no need for set(arr)
            for x in arr:
                counts[x] += 1

        # Now scan 1…100; if counts[i] == n_lists, it appeared in _every_ list
        res = []
        for val in range(1, 1001):
            if counts[val] == n_lists:
                res.append(val)
        return res
