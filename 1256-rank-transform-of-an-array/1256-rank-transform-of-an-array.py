class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))

        rankMap = {}
        result = []

        for i, num in enumerate(temp):
            if num not in rankMap:
                rankMap[num] = i+1
        
        for num in arr:
            result.append(rankMap[num])
        
        return result

