class Solution:
    def partitionString(self, s: str) -> int:
        word=""
        p=[]
        for i in s:
            if i not in word:
                word+=i
            else:
                p.append(word)
                word=i
        return len(p)+1