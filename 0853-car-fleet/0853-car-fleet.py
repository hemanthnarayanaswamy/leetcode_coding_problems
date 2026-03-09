class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = sorted(zip(position, speed), reverse=True)
        stack = []

        for p,s in order:
            t = (target - p)/s

            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
