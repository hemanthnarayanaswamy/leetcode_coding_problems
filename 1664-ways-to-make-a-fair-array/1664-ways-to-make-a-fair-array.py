class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        oddSum = sum([nums[i] for i in range(n) if i % 2])
        evenSum = total - oddSum
        post_odd = []
        post_even = []

        for i in range(n):
            if i % 2:
                oddSum -= nums[i]
            else:
                evenSum -= nums[i]
            
            post_odd.append(oddSum)
            post_even.append(evenSum)
        
        preOdd = preEven = res = 0

        for i in range(n):
            if preOdd + post_even[i] == preEven + post_odd[i]:
                res += 1
            
            if i % 2:
                preOdd += nums[i]
            else:
                preEven += nums[i]
            
        return res