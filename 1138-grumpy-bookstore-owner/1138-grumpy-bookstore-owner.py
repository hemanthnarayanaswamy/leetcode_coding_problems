class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        initialSatified = sum(c for c,g in zip(customers, grumpy) if not g)
        maxSatified = initialSatified
        
        for i in range(len(customers)-minutes+1):
            tmp = initialSatified
            for j in range(i, i + minutes):
                if grumpy[j]:
                    tmp += customers[j]
            
            if tmp > maxSatified:
                maxSatified = tmp
        
        return maxSatified