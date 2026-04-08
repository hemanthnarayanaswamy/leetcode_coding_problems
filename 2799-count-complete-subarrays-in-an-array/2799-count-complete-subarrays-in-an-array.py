class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        k = len(set(nums))
        left = 0
        count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1

            while len(freq) == k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    freq[nums[left]] += 1
                    break
                left += 1

            if len(freq) == k:
                count += left + 1

        return count