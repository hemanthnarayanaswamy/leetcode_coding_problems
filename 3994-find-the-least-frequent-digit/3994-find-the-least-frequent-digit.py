class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        nFreq = Counter(n)
        minFreq = len(n)
        answer = inf

        for num, f in nFreq.items():
            num = int(num)
            if f < minFreq:
                minFreq = f
                answer = num
            elif f == minFreq:
                if num < answer:
                    answer = num
        
        return answer
