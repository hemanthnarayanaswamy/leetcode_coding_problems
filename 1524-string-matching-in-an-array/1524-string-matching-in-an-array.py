class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        
        # sort ascending by length
        words_sorted = sorted(words, key=len)

        for i, w in enumerate(words_sorted):
            # only check against words longer than w
            for longer in words_sorted[i+1:]:
                if w in longer:
                    res.add(w)
                    break        # no need to check other longer words

        return list(res)
