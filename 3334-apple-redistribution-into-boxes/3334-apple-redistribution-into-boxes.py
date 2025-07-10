class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        capacitySorted = sorted(capacity, reverse = True)

        totalApples = sum(apple)

        box = 0

        while totalApples > 0:
            totalApples -= capacitySorted[box]
            box += 1
        
        return box

        

