class Solution:
    def reformat(self, s: str) -> str:
        alphabets = []
        nums = []

        for char in s:
            if char.isnumeric():
                nums.append(char)
            else:
                alphabets.append(char)

        a, n = len(alphabets), len(nums)

        if abs(a-n) == 1:
            if a > n:
                return "".join([alp+num for alp,num in zip(alphabets, nums)]) + alphabets[-1]
            elif a < n:
                return "".join([num+alp for alp,num in zip(alphabets, nums)]) + nums[-1]
        elif a - n == 0:
            return "".join([num+alp for alp,num in zip(alphabets, nums)])
        else:
            return ''