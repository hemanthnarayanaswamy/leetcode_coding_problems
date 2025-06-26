class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniNum = set()

        for num in nums: 
            if num and num not in uniNum:
                uniNum.add(num)
        
        return len(uniNum)
