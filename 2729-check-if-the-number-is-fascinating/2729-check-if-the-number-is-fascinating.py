class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n * 2
        n3 = n * 3
    
        conStr = Counter(str(n) + str(n2) + str(n3))
        print(conStr)
        
        if '0' in conStr or len(conStr) != 9:
            return False
        
        for _, val in conStr.items():
            if val > 1:
                return False
        
        return True