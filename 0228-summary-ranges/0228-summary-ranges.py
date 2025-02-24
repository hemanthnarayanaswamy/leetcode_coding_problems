class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if nums:
            start = end = nums[0]
        else:
            return result 
            
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(f"{end}")
                else:
                    result.append(f"{start}->{end}")
                start = end = nums[i]
            
        if start == end:
            result.append(f"{end}")
        else:
            result.append(f"{start}->{end}")

        return result
        