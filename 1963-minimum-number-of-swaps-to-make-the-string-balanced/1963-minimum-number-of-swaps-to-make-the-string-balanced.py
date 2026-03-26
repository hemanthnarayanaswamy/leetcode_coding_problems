class Solution:
    def minSwaps(self, s: str) -> int:
        s = list(s)
        brackets = {'[': 0, ']': 0}
        l, r = 0, len(s)-1
        swaps = 0

        while l < r:
            brackets[s[l]] += 1

            while brackets[']'] > brackets['[']:
                if s[l] == ']' and s[r] == '[':
                    s[l], s[r] = s[r], s[l]
                    brackets['['] += 1
                    brackets[']'] -= 1
                    swaps += 1
                else:
                    r -= 1  
            l += 1
        
        return swaps


