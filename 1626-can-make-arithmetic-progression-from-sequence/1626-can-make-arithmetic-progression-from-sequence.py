class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff = set()

        for i in range(1, len(arr)):
            diff.add(arr[i] - arr[i-1])
        
        return True if len(diff) == 1 else False