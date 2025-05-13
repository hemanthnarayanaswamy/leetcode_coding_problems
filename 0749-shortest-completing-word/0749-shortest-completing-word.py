class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp = Counter(''.join(i for i in licensePlate.lower().replace(" ", "") if not i.isdigit()))
        result = None

        for word in words:
            temp = Counter(word)
            if all(temp.get(c, 0) >= lp[c] for c in lp):
                if result is None or len(word) < len(result):
                    result = word

        return result

