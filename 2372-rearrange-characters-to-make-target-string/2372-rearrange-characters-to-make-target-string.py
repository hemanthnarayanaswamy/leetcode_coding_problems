class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target = Counter(target)
        s = {k:v for (k, v) in Counter(s).items() if k in target}

        for char in target:
            if char not in s:
                return 0
            else:
                s[char] = (s[char] // target[char])
        
        return min(s.values())

        