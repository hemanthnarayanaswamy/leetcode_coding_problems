class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        specialFreq = defaultdict(int)
        def stringSort(word):
            n = len(word)
            sortedWord = ''.join(sorted(word[0:n:2])) + ''.join(sorted(word[1:n:2]))
            return sortedWord

        for word in words:
            formatedWord = stringSort(word)
            specialFreq[formatedWord] += 1

        return len(specialFreq)
