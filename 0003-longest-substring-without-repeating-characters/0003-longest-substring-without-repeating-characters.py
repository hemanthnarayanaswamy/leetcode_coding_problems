class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        count = 0
        max_count = 0
        l, r = 0,0
        while l < len(s) and r < len(s):
            if s[r] not in str_set:
                str_set.add(s[r])
                r += 1
                count += 1
            else:
                str_set.clear()
                l += 1
                r = l 
                count = 0
            max_count = max(max_count, count)
        
        return max_count
        