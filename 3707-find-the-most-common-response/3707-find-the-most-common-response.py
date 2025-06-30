class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq_map = {}
        highest_freq = -1
        highest_freq_word = ""
        for l in responses:
            used_words = set()
            for word in l:
                if word in used_words:
                    continue
                if word in freq_map:
                    freq_map[word] += 1
                else:
                    freq_map[word] = 1
                used_words.add(word)
        for key, val in freq_map.items():
            if val > highest_freq:
                highest_freq = val
                highest_freq_word = key
            elif val == highest_freq:
                highest_freq_word = min(key, highest_freq_word)
        return highest_freq_word