class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitsFreq = defaultdict(int)
        startIdx = 0
        ans = 0

        for end, fruit in enumerate(fruits):
            fruitsFreq[fruit] += 1

            if len(fruitsFreq) > 2:
                fruitsFreq[fruits[startIdx]] -= 1

                if fruitsFreq[fruits[startIdx]] == 0:
                    del fruitsFreq[fruits[startIdx]]
                
                startIdx += 1
                ans = max(ans, end - startIdx + 1)
            
            
        
        return max(ans, end - startIdx + 1)
