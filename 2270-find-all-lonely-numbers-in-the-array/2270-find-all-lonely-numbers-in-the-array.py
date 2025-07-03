class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [
            x
            for x, c in freq.items()
            if c == 1
            and (x - 1) not in freq
            and (x + 1) not in freq
        ]
