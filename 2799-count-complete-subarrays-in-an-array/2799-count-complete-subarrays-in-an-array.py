class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        k = len(set(nums))
        left = 0
        count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1

            while len(freq) == k:
                count += (n - i)
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return count