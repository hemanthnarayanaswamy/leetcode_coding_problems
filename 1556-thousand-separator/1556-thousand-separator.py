class Solution:
    def thousandSeparator(self, n: int) -> str:
        nStr = str(n)
        res = []
        
        count = 0
        for i in range(len(nStr)-1, -1, -1):
            res.append(nStr[i])
            count += 1

            if count == 3 and i != 0:
                res.append('.')
                count = 0
        print(res[::-1])

        return ''.join(res[::-1])


