class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        sol=[]
        for num in nums:
            if num > 9:
                for digit in str(num):
                    sol.append(int(digit))
            else:
                sol.append(num)
        return sol