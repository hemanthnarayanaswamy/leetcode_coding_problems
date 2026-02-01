class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        m1 = m2 = float('inf')
        minCost = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < m1:
                m2 = m1
                m1 = nums[i]
                print(m1, m2)
            elif nums[i] < m2:
                m2 = nums[i]
        
        minCost += (m1 + m2)
       
        return minCost
