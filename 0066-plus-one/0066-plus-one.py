class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse from the last digit
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1  # Increment the current digit
                return digits  # Return early (no need to modify other digits)
            digits[i] = 0  # Set current digit to 0 (carry to next)

        # If all digits were 9 (e.g., [9,9,9] → [1,0,0,0])
        return [1] + digits
        