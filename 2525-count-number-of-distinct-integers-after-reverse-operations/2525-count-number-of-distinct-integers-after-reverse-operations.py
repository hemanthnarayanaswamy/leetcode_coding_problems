class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        def reversedIntegers(num):
            x = 0
            while num:
                digit = num % 10 # Extract the last digit 
                x = 10 * x + digit
                num //= 10  # Remove last digit from num
            return x

        distinctInt = set()

        for num in nums:
            rev = reversedIntegers(num)
            distinctInt.add(num)
            distinctInt.add(rev)
        
        return len(distinctInt)
