class Solution:
    def oddString(self, words: List[str]) -> str:
        def get_difference_array(word):
            return tuple(ord(word[i]) - ord(word[i-1]) for i in range(1, len(word)))
        
        diff_map = {}
        
        for word in words:
            diff = get_difference_array(word)
            if diff in diff_map:
                diff_map[diff].append(word)
            else:
                diff_map[diff] = [word]
        
        for words_list in diff_map.values():
            if len(words_list) == 1:
                return words_list[0]