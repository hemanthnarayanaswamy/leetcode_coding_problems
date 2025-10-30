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
        
        i = 0
        gainSatified = sum(gain[i:i+minutes])        
        maxSatified = initialSatified + gainSatified

        print(gain, initialSatified)
    
        while i < len(gain)-minutes:
            i += 1
            gainSatified = gainSatified - gain[i-1] + gain[i+minutes-1]
            maxSatified = max(maxSatified, initialSatified+gainSatified)
        
        return maxSatified
            

