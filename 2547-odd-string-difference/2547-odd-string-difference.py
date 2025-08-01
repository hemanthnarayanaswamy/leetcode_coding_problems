class Solution:
    def oddString(self, words: List[str]) -> str:
        from collections import defaultdict
        
        diff_count = defaultdict(list)
        
        for word in words:
            diff = tuple(ord(word[i]) - ord(word[i-1]) for i in range(1, len(word)))
            diff_count[diff].append(word)
        
        return next(words[0] for words in diff_count.values() if len(words) == 1)