class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        all_apples = sum(apple)
        capacity.sort()
        boxes = 0

        for c in capacity[::-1]:
            if all_apples > 0:
                all_apples -= c
                boxes += 1
            else:
                break
        return boxes
