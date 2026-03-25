class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledgeMap = {k: v for k,v in knowledge}
        res = []
        question = '?'
        i = 0

        while i < len(s):
            c = s[i]
            if c == '(':
                i += 1
                start = i
                while s[i] != ')':
                    i += 1
                end = i
                i += 1
                tmp = knowledgeMap.get(s[start:end], question)
                res.append(tmp)
            else:
                res.append(c)
                i += 1
        
        return ''.join(res)