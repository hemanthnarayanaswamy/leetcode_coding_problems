class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        targetSet = set(target)
        lastElement = max(target)
        res = []

        for i in range(1, lastElement+1):
            if i in targetSet:
                res.append('Push')
            else:
                res.append('Push')
                res.append('Pop')
        
        return res
            
        

            

            



