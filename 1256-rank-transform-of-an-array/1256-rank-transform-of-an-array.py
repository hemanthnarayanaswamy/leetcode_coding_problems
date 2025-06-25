class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))

        rankMap = {num: i+1 for i, num in enumerate(temp)}
        
        
        return [rankMap[num] for num in arr]

