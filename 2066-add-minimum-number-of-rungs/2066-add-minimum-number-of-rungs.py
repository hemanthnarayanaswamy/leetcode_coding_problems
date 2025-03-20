class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        i = 0
        addons = 0
        current_step = 0
        while current_step != rungs[-1] and i < len(rungs):
            next_step = rungs[i]
            ## print(current_step, next_step, i)
            if abs(next_step - current_step)  <= dist:
                current_step = next_step
                i += 1
            else:
                addons += ((next_step - current_step) - 1) // dist
                current_step = next_step
                i += 1
        return addons
        