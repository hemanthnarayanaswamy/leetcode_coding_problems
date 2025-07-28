class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        targetSet = set(target)
        lastElement = max(target)
        res = []

        for i in range(1, lastElement+1):
            res.append('Push')

            if i not in targetSet:
                res.append('Pop')
        
        return res
            
        

            

            



