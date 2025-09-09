class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * len(code)

        if k > 0:
            initialSum = sum(code[:k])
            for i in range(n):
                res[i] = initialSum - code[i] + code[(i+k) % n]
                initialSum = res[i]
        elif k < 0:
            k = -k
            code = code[::-1]
            initialSum = sum(code[:k])
            for i in range(n):
                res[i] = initialSum - code[i] + code[(i+k) % n]
                initialSum = res[i]
            
            res = res[::-1]
        
        return res

