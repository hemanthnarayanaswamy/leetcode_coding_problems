class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrence = []
        res = []

        for i, num in enumerate(nums):
            if num == x:
                occurrence.append(i)
        
        no = len(occurrence)
        for q in queries:
            if q > no:
                res.append(-1)
            else:
                res.append(occurrence[q-1])
        
        return res
