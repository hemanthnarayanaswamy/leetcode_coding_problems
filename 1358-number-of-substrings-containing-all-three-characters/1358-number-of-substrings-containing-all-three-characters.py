class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        track = defaultdict(int)
        subcount = 0
        left = 0

        for right, c in enumerate(s):
            track[c] += 1

            while len(track) == 3 and track[s[left]] > 1:
                track[s[left]] -= 1
                left += 1
            
            if len(track) == 3:
                subcount += (left + 1)
        
        return subcount