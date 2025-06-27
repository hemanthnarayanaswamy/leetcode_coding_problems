class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        nums.sort()

        for index, value in enumerate(nums):
            if value == target:
                my_list.append(index)

        return my_list
        