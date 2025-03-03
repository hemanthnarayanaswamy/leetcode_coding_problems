class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix_product = [1]
        postfix_product = [1]


        for i in range(1, len(nums)):
            prefix_product.append(prefix_product[i-1]*nums[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            postfix_product.append(postfix_product[-1]*nums[i+1])
            
        postfix_product = postfix_product[::-1]

        for i in range(len(nums)):
            result.append(prefix_product[i]*postfix_product[i])
        

        return result
        