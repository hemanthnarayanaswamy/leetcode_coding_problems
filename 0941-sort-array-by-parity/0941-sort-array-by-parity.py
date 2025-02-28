class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_array = []
        odd_array = []
        for num in nums:
            if num % 2 == 0:
                even_array.append(num)
            else: 
                odd_array.append(num)
        return even_array + odd_array
        