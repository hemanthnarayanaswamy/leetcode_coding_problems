class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        temp = set()

        for c in s:
            if c in temp:
                count += 1
                temp.clear()
                temp.add(c)
            else:
                temp.add(c)
        count += 1
        
        return count