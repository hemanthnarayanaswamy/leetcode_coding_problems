class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = list(words[0])
        for word in words[1:]:
            new_result = []
            for ch in word:
                if ch in result:
                    new_result.append(ch)
                    result.remove(ch)
            result = new_result
        return result