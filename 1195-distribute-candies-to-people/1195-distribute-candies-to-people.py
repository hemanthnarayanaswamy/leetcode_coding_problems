class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        counter = 1

        while candies > 0:
            for i in range(num_people):
                if candies > 0:
                    res[i] += min(counter, candies)
                    candies -= counter
                    counter += 1 

        return res
