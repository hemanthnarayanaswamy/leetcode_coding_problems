class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def separateNum(num):
            arr = []
            while num:
                num, m = divmod(num, 10)
                arr.append(m)
            return arr[::-1]
        
        res = []
        for num in nums:
            res.extend(separateNum(num))
        
        return res