class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  # Difference array
        
        # Step 1: Process all shifts in O(m) time
        for start, end, direction in shifts:
            shift_val = 1 if direction == 1 else -1
            diff[start] += shift_val
            diff[end + 1] -= shift_val
        
        # Step 2: Convert to actual shift values in O(n) time
        actual_shifts = [0] * n
        actual_shifts[0] = diff[0]
        for i in range(1, n):
            actual_shifts[i] = actual_shifts[i-1] + diff[i]
        
        # Step 3: Apply shifts to characters in O(n) time
        result = []
        for i in range(n):
            shifted_val = (ord(s[i]) - ord('a') + actual_shifts[i]) % 26
            result.append(chr(shifted_val + ord('a')))
        
        return ''.join(result)
            