class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_greater = []
        pivot_lesser = [] 
        pivot_equal = []

        for num in nums:
            if num > pivot:
                pivot_greater.append(num)
            elif num < pivot:
                pivot_lesser.append(num)
            else:
                pivot_equal.append(num)
        
        return pivot_lesser+pivot_equal+pivot_greater

        