class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        # keep subtracting the smaller from the larger in bulk
        while num1 and num2:
            if num1 >= num2:
                # subtract num2 as many times as possible in one go
                q, num1 = divmod(num1, num2)  # does the same in one C-level operation (q = num1 // num2 and num1 %= num2).
                count += q
            else:
                q, num2 = divmod(num2, num1)
                count += q
        return count
