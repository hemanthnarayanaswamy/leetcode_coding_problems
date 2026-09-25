class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def convert(arr):
            opex = sum([arr[i+1]-arr[i] for i in range(0, len(arr), 2)])
                    
            if opex > k:
                return False
            
            return True

        n = len(nums)
        arr1 = []
        arr2 = []

        for i, num in enumerate(nums):
            if num == 1:
                arr1.append(i)
            else:
                arr2.append(i)

        n1 = len(arr1)
        n2 = n - n1
        
        if n1 == n or n2 == n:
            return True

        R1 = False if n1 % 2 else convert(arr1)
        R2 = False if n2 % 2 else convert(arr2)

        return R1 or R2
        
        
        
        return convert(arr1, n1) or convert(arr2, )