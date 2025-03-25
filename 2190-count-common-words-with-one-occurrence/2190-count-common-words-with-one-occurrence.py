from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        words1_freq = Counter(words1)
        words2_freq = Counter(words2)
        print(words1_freq,words2_freq )

        for word in words1_freq:
            if word not in words2_freq:
                continue
            elif words1_freq[word] > 1 or words2_freq[word] > 1:
                continue
            else:
                count += 1
        return count
        