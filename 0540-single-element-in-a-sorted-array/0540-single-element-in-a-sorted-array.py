class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2 
            if mid + 1 < len(nums):
                if mid % 2 == 0 and nums[mid] == nums[mid+1]:
                    l = mid + 1
                elif mid % 2 and nums[mid] == nums[mid+1]:
                    r = mid - 1
                elif mid % 2 and nums[mid] == nums[mid-1]:
                    l = mid + 1
                elif mid % 2 == 0 and nums[mid] == nums[mid - 1]:
                    r = mid - 1
                else:
                    return nums[mid]
            else:
                return nums[mid]


        return nums[mid]