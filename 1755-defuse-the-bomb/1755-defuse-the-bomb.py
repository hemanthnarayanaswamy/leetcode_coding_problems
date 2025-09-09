class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n

        if k == 0:
            return res 
        
        if k > 0:
            window_sum = sum(code[1:k+1])
        else:
            window_sum = sum(code[k:])
        
        res[0] = window_sum 

        for i in range(1, n):
            if k > 0:
                window_sum = window_sum - code[i] + code[(i + k) % n]
            else:
                # add new leftmost (Previous element) and remove 
                window_sum = window_sum - code[(i + k - 1) % n] + code[i - 1]
            
            res[i] = window_sum
        
        return res
