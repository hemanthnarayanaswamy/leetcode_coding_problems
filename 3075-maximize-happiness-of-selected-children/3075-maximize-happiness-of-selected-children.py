class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        maxHappy = 0
        
        for i in range(len(happiness)):
            if k:
                tmp = happiness[i] - i 
                if tmp > 0:
                    maxHappy += tmp
            k -= 1
            if k == 0:
                break

        return maxHappy
        