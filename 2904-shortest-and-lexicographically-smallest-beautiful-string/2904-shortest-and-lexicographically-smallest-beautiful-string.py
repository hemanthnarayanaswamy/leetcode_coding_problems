class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''

        left = 0 
        cnt1 = 0
        res = s

        for right, x in enumerate(s):
            cnt1 += int(x)
            
            while cnt1 > k or s[left] == '0':
                cnt1 -= int(s[left]) 
                left += 1
            
            if cnt1 == k: 
                curr = s[left:right+1]
                if len(curr) < len(res) or (len(res) == len(curr) and curr < res):
                    res = curr
                
        return res
