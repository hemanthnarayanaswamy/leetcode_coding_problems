class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        nums_in_ranges = set()

        for l, r in ranges:
            for num in range(l, r+1):
                nums_in_ranges.add(num)
        
        for num in range(left, right+1):
            if num not in nums_in_ranges:
                return False
        
        return True
