class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        gain = []
        initialSatified = 0
    
        for c,g in zip(customers, grumpy):
            if not g:
                initialSatified += c
                gain.append(0)
            else:
                gain.append(c)
        
        if minutes == 0:
            return initialSatified
        
        newSatified = sum(gain[:minutes]) +  initialSatified      
        maxSatified = newSatified
    
        for i in range(1, len(gain)-minutes+1):
            newSatified += gain[i+minutes-1] - gain[i-1]
            
            if newSatified > maxSatified:
                maxSatified = newSatified
        
        return maxSatified
            

