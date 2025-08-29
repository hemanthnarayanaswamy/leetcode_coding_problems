class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]

        if (a + b <= c) or (a + c <= b) or (b+ c <= a):
            return "none"
        elif a == b == c:
            return 'equilateral'
        elif (a == b) or (b == c) or (a == c):
            return 'isosceles'
        else:
            return 'scalene'