class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        nonNeg = []
        n = len(nums)

        for i in range(n):
            if nums[i] >= 0:
                nonNeg.append(nums[i])
                nums[i] = 'x'
        
        if not nonNeg:
            return nums
        
        k = k % len(nonNeg)
        nonNeg = nonNeg[k:] + nonNeg[:k]

        for i in range(n-1, -1, -1):
            if nums[i] == 'x':
                nums[i] = nonNeg.pop()

        return nums