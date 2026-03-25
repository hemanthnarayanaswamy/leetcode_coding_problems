class Solution:
    def evaluate(self, st: str, knowledge: List[List[str]]) -> str:
        d = {k:v for k, v in knowledge}
        s = st.split('(')
        res = [s[0]]

        for i in range(1, len(s)):
            a, b = s[i].split(')')
            res.append(d.get(a, '?') + b)
        
        return ''.join(res)

