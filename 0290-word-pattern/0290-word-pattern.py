class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        # Dictionaries to store mappings
        pattern_to_word = {}
        word_to_pattern = {}

        for i in range(len(pattern)):
            p, w = pattern[i], words[i]

            # Check existing mappings
            if p in pattern_to_word and pattern_to_word[p] != w:
                return False
            if w in word_to_pattern and word_to_pattern[w] != p:
                return False

            # Create new mappings
            pattern_to_word[p] = w
            word_to_pattern[w] = p

        return True