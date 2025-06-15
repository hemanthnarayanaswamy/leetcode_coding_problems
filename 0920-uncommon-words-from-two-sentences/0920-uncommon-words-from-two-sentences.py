class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combinedString = s1.split() + s2.split()

        result = [ch for ch, val in Counter(combinedString).items() if val == 1]

        print(result)

        return result

        

