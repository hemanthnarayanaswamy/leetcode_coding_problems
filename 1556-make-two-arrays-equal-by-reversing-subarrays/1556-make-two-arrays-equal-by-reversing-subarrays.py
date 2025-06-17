class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = {}
        # Count each value in target
        for x in target:
            count[x] = count.get(x, 0) + 1

        # Subtract counts for arr, bail out if anything goes negative or missing
        for y in arr:
            if count.get(y, 0) == 0:
                return False
            count[y] -= 1

        return True
