class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive_arr = [] 
        negative_arr = []
        result = []

        for num in nums:
            if num < 0:
                negative_arr.append(num)
            else:
                postive_arr.append(num)
        
        for pos, neg in zip(postive_arr, negative_arr):
            result.append(pos)
            result.append(neg)

        return result
        