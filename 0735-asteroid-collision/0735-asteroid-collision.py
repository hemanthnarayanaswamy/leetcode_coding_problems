class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0

        while i < len(asteroids):
            leftA = asteroids[i]
            if stack and (stack[-1] > 0 and leftA < 0):
                rightA = stack[-1]
                if rightA < -leftA:
                    stack.pop()
                elif rightA > -leftA:
                    i += 1
                else:
                    stack.pop()
                    i += 1
            else:
                stack.append(leftA)
                i += 1

        return stack