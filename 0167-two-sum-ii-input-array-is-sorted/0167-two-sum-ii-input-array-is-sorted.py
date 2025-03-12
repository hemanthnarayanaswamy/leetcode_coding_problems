class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(numbers)):
            if numbers[i] in result:
                return [result[numbers[i]], i+1]
            else:
                comp_diff = target - numbers[i]
                result[comp_diff] = i+1
        return []
        