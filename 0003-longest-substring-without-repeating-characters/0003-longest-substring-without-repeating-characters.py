class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        l = 0

        for r in range(len(s)):  # Expand right pointer
            while s[r] in char_set:  # If duplicate found, shrink from left
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])  # Add new character
            sublen =  r - l + 1
            if max_length < sublen:
                max_length = sublen  # Update max length
        
        return max_length
