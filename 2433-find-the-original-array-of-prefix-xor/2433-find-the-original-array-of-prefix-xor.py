class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev = 0
        result = []

        for num in pref:
            result.append(num ^ prev)
            prev = num
            
        return result