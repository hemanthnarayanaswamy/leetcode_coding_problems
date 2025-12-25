class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        maxHappy = 0
        
        for i in range(len(happiness)):
            if k:
                tmp = happiness[i] - i 
                k -= 1
                if tmp > 0:
                    maxHappy += tmp
            else:
                break
        
        return maxHappy