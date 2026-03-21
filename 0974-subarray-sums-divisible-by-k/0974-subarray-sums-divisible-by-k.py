class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        pre = 0
        subLen = 0

        for num in nums:
            pre += num
            rem = pre % k

            if not rem:
                subLen += 1
            
            subLen += freq[rem]

            freq[rem] += 1

        return subLen