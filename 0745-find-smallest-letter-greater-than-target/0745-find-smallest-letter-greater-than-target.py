class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        targetNum = ord(target)

        for c in letters:
            if ord(c) > targetNum:
                return c
        
        return letters[0]
