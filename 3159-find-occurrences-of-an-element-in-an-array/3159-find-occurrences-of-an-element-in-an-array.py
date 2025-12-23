class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ocs = [i for i, v in enumerate(nums) if v == x]
        n = len(ocs)

        ret = [ocs[q - 1] if q <= n else -1 for q in queries]

        return ret