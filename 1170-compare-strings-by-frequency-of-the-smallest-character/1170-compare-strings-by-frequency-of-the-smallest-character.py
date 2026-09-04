class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        def f(s):
            freq = Counter(s)
            for letter in letters:
                if letter in freq:
                    return freq[letter]
        
        arrW = []
        for w in words:
            arrW.append(f(w))
        
        valMap = Counter(arrW)
        res = []

        for q in queries:
            x = f(q)
            count = 0

            for k, v in valMap.items():
                if x < k:
                    count += v
            
            res.append(count)
        
        return res