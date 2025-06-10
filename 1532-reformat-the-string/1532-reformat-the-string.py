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

        if a - n == 1:
            return "".join([alp+num for alp,num in zip(alphabets, nums)]) + alphabets[-1]
        elif n - a == 1:
            return "".join([num+alp for alp,num in zip(alphabets, nums)]) + nums[-1]
        elif a - n == 0:
            return "".join([num+alp for alp,num in zip(alphabets, nums)])
        else:
            return ''