class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) == len(arr):
            targetFreq = Counter(target)
            arrFreq = Counter(arr)
            return targetFreq == arrFreq
        else:
            return False