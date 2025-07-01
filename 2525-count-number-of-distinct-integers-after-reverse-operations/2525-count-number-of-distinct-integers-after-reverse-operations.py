class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinctInt = set(nums)

        for num in nums:
            if num > 9:
                rev = int(str(num)[::-1])
                distinctInt.add(rev)
        
        return len(distinctInt)
