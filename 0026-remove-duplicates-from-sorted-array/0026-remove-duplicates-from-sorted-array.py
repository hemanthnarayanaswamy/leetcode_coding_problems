class Solution:
    def removeDuplicates(self, list: List[int]) -> int:
        l = 0
        for r in range(1, len(list)):
            if list[l] != list[r]:
                l += 1
                list[l] = list[r]
        return l + 1
