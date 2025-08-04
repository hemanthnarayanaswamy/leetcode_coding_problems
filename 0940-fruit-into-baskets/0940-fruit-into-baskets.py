class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsFreq = Counter()
        startIdx = 0
        ans = 0

        for i, fruit in enumerate(fruits):
            fruitsFreq[fruit] += 1

            while len(fruitsFreq) > 2:
                fruitsFreq[fruits[startIdx]] -= 1

                if fruitsFreq[fruits[startIdx]] == 0:
                    del fruitsFreq[fruits[startIdx]]
                
                startIdx += 1
            
            ans = max(ans, i - startIdx + 1)
        
        return ans
