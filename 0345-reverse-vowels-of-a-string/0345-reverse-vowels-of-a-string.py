class Solution:
    def reverseVowels(self, s: str) -> str:
        s= list(s)
        vowels = {'a','e','i','o','u'}
        left, right = 0, len(s)-1
        while left < right:
            left_char = s[left]
            right_char = s[right]
            if right_char.lower() in vowels and left_char.lower() in vowels:
                s[left], s[right] = right_char, left_char
                left += 1
                right -= 1
            elif right_char.lower() in vowels and left_char.lower() not in vowels:
                left += 1
            else:
                right -= 1

        return ''.join(s)
        