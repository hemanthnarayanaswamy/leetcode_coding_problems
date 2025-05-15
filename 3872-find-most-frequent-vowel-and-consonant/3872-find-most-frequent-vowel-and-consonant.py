class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxV, maxC = 0, 0
        s = Counter(s)
        vowels = {'a','e','i','o','u'}

        for char, val in s.items():
            if char in vowels:
                if val > maxV:
                    maxV = val
            else:
                if val > maxC:
                    maxC = val
        
        return maxV + maxC
