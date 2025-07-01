class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def reversedIntegers(num):
            x = 0
            while num:
                digit = num % 10 # Extract the last digit 
                x = 10 * x + digit
                num //= 10  # Remove last digit from num
            return x

        distinctInt = set(nums)

        for num in nums:
            rev = reversedIntegers(num)

            if rev not in distinctInt:
                distinctInt.add(rev)
        
        return len(distinctInt)
