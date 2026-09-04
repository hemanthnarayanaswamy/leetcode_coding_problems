class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        def f(s):
            freq = Counter(s)
            for letter in letters:
                if letter in freq:
                    return freq[letter]
        
        arrW = []
        n = len(words)

        for w in words:
            arrW.append(f(w))
        
        arrW.sort()
        res = []

        for q in queries:
            x = f(q)

            l, r = 0, n
            while l < r:
                m = (l + r) // 2

                if arrW[m] <= x:
                    l = m + 1
                else:
                    r = m
            
            res.append(n - l) 
        
        return res

