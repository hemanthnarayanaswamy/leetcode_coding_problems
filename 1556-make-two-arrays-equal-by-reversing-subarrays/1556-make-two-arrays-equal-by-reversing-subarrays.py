class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        targetFreq = Counter(target)
        arrFreq = Counter(arr)

        return targetFreq == arrFreq