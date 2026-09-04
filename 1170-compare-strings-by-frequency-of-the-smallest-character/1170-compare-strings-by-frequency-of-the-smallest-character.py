class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            freq = Counter(s)
            for i in range(ord('a'), ord('z')+1):
                c = chr(i)
                if c in freq:
                    return freq[c]
        
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
        
        print(arrW, valMap)
        return res

