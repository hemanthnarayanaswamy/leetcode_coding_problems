class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowelChars = {'a', 'e', 'i', 'o', 'u'}

        for i in range(left, right+1):
            if words[i][0] in vowelChars and words[i][-1] in vowelChars:
                count += 1
        
        return count
