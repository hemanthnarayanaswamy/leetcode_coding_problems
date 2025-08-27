class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        preMid = 0

        if nums[l] == target: return l
        if nums[r] == target: return r

        while l <= r:
            mid = (l+r)//2
            print(nums[mid])
            if mid == preMid:
                break
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
            
            preMid = mid
        
        if target > nums[r]:
            return r + 1
        elif target < nums[l]:
            return l
        else:
            return l + 1