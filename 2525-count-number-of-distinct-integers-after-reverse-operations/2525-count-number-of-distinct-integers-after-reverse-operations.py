class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinctInt = nums[::]

        for num in nums:
            if num > 9:
                distinctInt.append(int(str(num)[::-1]))
        
        return len(set(distinctInt))
