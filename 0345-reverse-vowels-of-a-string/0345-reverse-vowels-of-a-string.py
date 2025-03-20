class Solution:
    def reverseVowels(self, s: str) -> str:
        s= list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  # Include uppercase vowels
        left, right = 0, len(s) - 1  # Two pointers

        while left < right:
            while left < right and s[left] not in vowels:  # Move left pointer to next vowel
                left += 1
            while left < right and s[right] not in vowels:  # Move right pointer to previous vowel
                right -= 1

            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)  # Convert list back to string
        