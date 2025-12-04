class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0

        for car in directions:
            # PART 1: Handle L or S cars meeting R cars
            if car == 'L' or car == 'S':
                while stack and stack[-1] == 'R':
                    stack.pop()
                    collisions += 1
                    if car == 'L':
                        collisions += 1
                        car = 'S'
            
            # PART 2: Handle L car meeting S car
            if car == 'L':
                if stack and stack[-1] == 'S':
                    collisions += 1
                    car = 'S'
            
            # PART 3: Push non-L cars to stack
            if car != 'L':
                stack.append(car)
        
        return collisions