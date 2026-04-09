class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        specialFreq = set()

        for word in words:
            n = len(word)
            formatedWord = ''.join(sorted(word[0:n:2])) + ''.join(sorted(word[1:n:2]))
            specialFreq.add(formatedWord)

        return len(specialFreq)
