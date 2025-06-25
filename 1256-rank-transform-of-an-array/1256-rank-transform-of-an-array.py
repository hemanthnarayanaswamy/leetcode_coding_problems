class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))

        rankMap = {num: i+1 for i, num in enumerate(temp)}
        result = []
        
        for num in arr:
            result.append(rankMap[num])
        
        return result

