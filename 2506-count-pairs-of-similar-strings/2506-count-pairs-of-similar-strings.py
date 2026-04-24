class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordChar = defaultdict(int)
        pairs = 0

        for word in words:
            key = tuple(sorted(set(word)))
            wordChar[key] += 1
        
        for n in wordChar.values():
            pairs += (n * (n-1))//2
        
        return pairs
        
