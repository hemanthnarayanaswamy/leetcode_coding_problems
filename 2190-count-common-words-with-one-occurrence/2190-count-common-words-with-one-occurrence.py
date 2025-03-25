from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        words1_freq = Counter(words1)
        words2_freq = Counter(words2)

        for word in words1_freq:
            if word in words2_freq and words1_freq[word] == words2_freq[word] == 1:
                count += 1
        
        return count
        