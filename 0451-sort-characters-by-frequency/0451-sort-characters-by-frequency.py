from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = Counter(s)
        sorted_chars = sorted(char_freq, key=char_freq.get, reverse=True)

        result = ''
        for char in sorted_chars:
            result += char * char_freq[char]

        return result

        