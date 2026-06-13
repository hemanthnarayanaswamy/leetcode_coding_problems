class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def wordWeightMap(word):
            weight = 0
            for c in word:
                weight += weights[ord(c) - 97]

            weight %= 26
            return chr(ord('z') - weight)

        res = ''

        for word in words:
            res += wordWeightMap(word)

        return res
            