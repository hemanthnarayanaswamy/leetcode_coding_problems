class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ones = nums.count(1)
        nones = n - ones

        if ones % 2 and nones % 2:
            return False
        
        if ones == n or nones == n:
            return True

        def convert(target):
            arr = []
            for i, num in enumerate(nums):
                if num == target:
                    arr.append(i)
            
            if len(arr) % 2:
                return False
            
            opex = sum([arr[i+1]-arr[i] for i in range(0, len(arr), 2)])
                    
            if opex > k:
                return False
            
            return True
        
        print(convert(1))
        print(convert(-1))
        return convert(1) or convert(-1)