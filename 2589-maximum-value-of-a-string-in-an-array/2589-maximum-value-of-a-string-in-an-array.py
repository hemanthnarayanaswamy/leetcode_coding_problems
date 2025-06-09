class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxValue = 0

        for s in strs:
            if s.isdigit():
                maxValue = max(maxValue, int(s))
            else:
                maxValue = max(maxValue, len(s))

        return maxValue