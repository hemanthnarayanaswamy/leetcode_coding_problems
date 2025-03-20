class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        i = 0       # Track Steps
        addons = 0  ## To track number of inserctions
        current_step = 0 ## Current Step
        while current_step != rungs[-1]:
            next_step = rungs[i]
            if abs(next_step - current_step)  > dist:
                addons += ((next_step - current_step) - 1) // dist
            current_step = next_step
            i += 1
        return addons
        