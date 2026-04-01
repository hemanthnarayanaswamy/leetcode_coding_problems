class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        def digits(n):
            dig = []
            while n:
                d, r = divmod(n, 10)
                dig.append(r)
                n = d
            return dig
        
        nums = digits(n)
        res = []
        
        for i in range(len(nums)-1, -1, -1):
            tmp = nums[i] * 10 ** i
            if tmp:
                res.append(tmp)
        return res
