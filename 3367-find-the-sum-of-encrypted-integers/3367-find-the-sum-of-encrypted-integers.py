class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:

        s = 0
        for n in nums:
            str_n = str(n)

            s += int(len(str_n) * max(str_n))
        return s