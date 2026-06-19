class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []

        for restaurant in restaurants:
            if restaurant[2] >= veganFriendly and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                res.append([restaurant[0], restaurant[1]])
            
            
        res = sorted(res, key=lambda row: (row[1], row[0]), reverse=True)
        return [r[0] for r in res]
