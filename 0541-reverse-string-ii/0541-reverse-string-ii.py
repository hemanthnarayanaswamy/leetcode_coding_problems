class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)         # Convert string to list to allow modifications
        n = len(s)

        # Process the string in chunks of 2k
        for i in range(0, n, 2 * k):
            left, right = i, min(i + k - 1, n - 1)  # Two pointers for reversing

            # Reverse first k characters using two-pointer swapping
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)  # Convert list back to string
             