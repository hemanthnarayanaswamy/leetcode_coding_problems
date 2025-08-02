class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)

        subseq = []
        subseq_sum = 0

        for x in nums:
            subseq_sum += x      
            total -= x         
            subseq.append(x)

            if subseq_sum > total:
                break

        return subseq

