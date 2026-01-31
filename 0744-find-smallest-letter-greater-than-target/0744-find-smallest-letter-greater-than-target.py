class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetNum = ord(target)
        n = len(letters)
        l, r = 0, n

        while l < r:
            m = (l + r) // 2
            if ord(letters[m]) > targetNum:
                r = m
            else: 
                l = m + 1
        
        return letters[l] if l < n else letters[0]
