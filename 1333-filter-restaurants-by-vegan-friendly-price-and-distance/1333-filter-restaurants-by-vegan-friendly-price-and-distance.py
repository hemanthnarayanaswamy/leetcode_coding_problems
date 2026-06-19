class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        restaurants = sorted(restaurants, key=lambda row: (row[1], row[0]), reverse=True)

        for restaurant in restaurants:
            id, r, v, p, d = restaurant

            if (veganFriendly and not v) or p > maxPrice or d > maxDistance:
                continue
            
            res.append(id)
        
        return res
