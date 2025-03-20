class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        addons = 0
        previous = 0
        for current in rungs:
            diff = current - previous
            if diff > dist:
                addons += (diff -1) // dist
            previous = current
        return addons
        