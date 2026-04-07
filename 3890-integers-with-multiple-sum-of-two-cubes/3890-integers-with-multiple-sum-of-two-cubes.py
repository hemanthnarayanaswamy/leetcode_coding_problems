class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        freq = defaultdict(int)
        limit = int(n**1/3)

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
        
        res = []
        for num, f in freq.items():
            if f > 1:
                res.append(num)
        
        return sorted(res)