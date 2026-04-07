class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        freq = defaultdict(int)
        limit = int(n**1/3)
        res = set()

        for i in range(limit):
            a = i ** 3
            if a >= n:
                break
            for j in range(i, limit):
                b = j ** 3
                x = a + b
                if x <= n:
                    freq[x] += 1  
                else:
                    break

                if freq[x] > 1:
                    res.add(x)      
        
        return sorted(res)