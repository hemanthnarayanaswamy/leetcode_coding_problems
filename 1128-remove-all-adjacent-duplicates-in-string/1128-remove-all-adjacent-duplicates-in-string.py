class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = []

        for i in range(len(s)):
            if len(result) == 0:
                result.append(s[i])

            elif result[-1] == s[i]:
                result.pop()

            else:
                result.append(s[i])
        
        return ''.join(result)