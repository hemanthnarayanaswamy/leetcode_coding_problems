class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        nums_map = {}
        
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        
        for num, count in nums_map.items():
            if count == 1:  # If only one occurrence, it's impossible
                return -1

            quotient = count // 3  # Number of full groups of 3
            remainder = count % 3  # Remaining elements after grouping by 3

            if remainder == 0:
                result += quotient  # Perfectly divisible by 3
            else:
                result += quotient + 1  # Need one extra operation (either a group of 2 or extra 3)

        return result
        