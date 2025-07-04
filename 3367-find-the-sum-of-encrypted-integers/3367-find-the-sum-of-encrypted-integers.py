class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num < 10:
                res += num 
            else:
                temp = list(str(num))
                maxDig = max(temp)
                encrypted_num = int(maxDig * len(temp))

                res += encrypted_num
        
        return res
                
