from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = Counter(s)
        sorted_chars = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)

        result = ''
        for char, count in sorted_chars:
            result += char * count

        return result

        