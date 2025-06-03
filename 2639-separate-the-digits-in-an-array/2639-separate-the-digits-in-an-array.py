class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for item in nums:
            digit_list = list(map(int, str(item)))
            answer.extend(digit_list)
        return answer