class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        longestSub = 0
        n = len(nums)

        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                if i != n-1:
                    l, r = i, i+1
                else:
                    l = r = i

                while r < n:
                    nl = nums[l]
                    nr = nums[r]
                    if (nl > threshold or nr > threshold) or (nl % 2 == nr % 2):
                        break
                    l += 1
                    r += 1
               
                print(i, l, r)
                longestSub = max(longestSub, l - i + 1)
        
        return longestSub
