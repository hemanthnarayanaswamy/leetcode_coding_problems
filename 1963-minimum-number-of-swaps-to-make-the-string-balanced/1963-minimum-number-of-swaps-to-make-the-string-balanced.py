class Solution:
    def minSwaps(self, s: str) -> int:
        unmatched = 0

        for ch in s:
            if ch == '[':
                unmatched +=1
            else:
                if unmatched > 0:
                    unmatched -= 1
                else:
                    unmatched += 1
        
        return (unmatched+1)//2

