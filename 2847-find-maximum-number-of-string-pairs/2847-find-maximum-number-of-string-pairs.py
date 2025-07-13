class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        uniq = set()
        count = 0

        for word in words:
            if word[::-1] in uniq:
               count += 1
            else:
                uniq.add(word)

        return count 
