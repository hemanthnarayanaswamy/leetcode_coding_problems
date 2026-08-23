class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary = ''

        for letter in s:
            ascii_value = bin(ord(letter))[2:]
            ascii_value = '0' * (8-len(ascii_value)) + ascii_value
            binary = binary + ascii_value
            
        return binary == binary[::-1]