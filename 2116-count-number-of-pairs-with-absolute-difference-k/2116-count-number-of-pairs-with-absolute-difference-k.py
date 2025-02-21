class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums_map = {}
        for num in nums: # we are counting the frequency of each number and tracking them 
            if num in nums_map:
                nums_map[num] += 1
            else:
                nums_map[num] = 1

        count = 0
        
        for num in nums:
            temp = num+k
            if temp in nums_map:
                count += nums_map[temp]
        return count
            