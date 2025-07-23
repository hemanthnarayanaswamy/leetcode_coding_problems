class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        counter = 1

        while candies:
            for i in range(num_people):
                if counter <= candies:
                    res[i] += counter
                    candies -= counter
                    counter += 1
                else:
                    res[i] += candies
                    return res

        return res
                    