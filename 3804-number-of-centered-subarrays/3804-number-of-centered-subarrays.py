class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            subelements = set()
            subSum = 0
            for j in range(i, n):
                num = nums[j]
                subelements.add(num)
                subSum += num

                if subSum in subelements:
                    res += 1
        
        return res

