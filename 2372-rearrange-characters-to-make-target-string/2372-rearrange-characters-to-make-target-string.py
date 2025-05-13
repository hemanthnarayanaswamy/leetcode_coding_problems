class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target = Counter(target)
        s = Counter(s)
        st = {k:v for (k, v) in s.items() if k in target}

        for char in target:
            if char not in st:
                return 0
            else:
                st[char] = (st[char] // target[char])
        
        return min(st.values())

        