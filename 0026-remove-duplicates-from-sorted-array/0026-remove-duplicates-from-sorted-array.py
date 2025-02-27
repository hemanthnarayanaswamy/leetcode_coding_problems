class Solution:
    def removeDuplicates(self, list: List[int]) -> int:
        l, r = 0, 1 
        while r < len(list):
            if list[l] == list[r]:
                list.pop(r)
            else:
                l = r
                r += 1
        return len(list)
        