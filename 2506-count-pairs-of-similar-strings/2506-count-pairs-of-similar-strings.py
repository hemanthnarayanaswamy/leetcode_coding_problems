class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordChar = {}
        pairs = 0

        for word in words:
            word
            key = tuple(sorted(set(word)))
            wordChar[key] = wordChar.get(key, 0) + 1
        
        for n in wordChar.values():
            pairs += (n * (n-1))//2
        
        return pairs
        
