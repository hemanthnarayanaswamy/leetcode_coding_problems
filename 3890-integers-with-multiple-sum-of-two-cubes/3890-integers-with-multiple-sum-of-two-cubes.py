class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        freq = defaultdict(int)
        limit = int(n**(1/3)) + 1
        res = set()

        for i in range(1, limit):
            a = i ** 3
            if a >= n:
                break
            for j in range(i, limit):
                b = j ** 3
                x = a + b
                if x <= n:
                    if x in freq and x not in res:
                        res.add(x)
                    else:
                        freq[x] = 1  
                else:
                    break       
        
        return sorted(res)