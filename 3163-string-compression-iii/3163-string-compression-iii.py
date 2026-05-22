class Solution:
    def compressedString(self, word: str) -> str:
        stack = []
        res = ''

        for i in range(len(word)):
            if stack:
                if stack[-1] == word[i]:
                    stack.append(word[i])
                    if len(stack) == 9:
                        res += f'9{stack[-1]}'
                        stack = []
                else:
                    res += f'{len(stack)}{stack[-1]}'
                    stack = [word[i]]
            else:
                stack.append(word[i])
        
        if stack:
            res += f'{len(stack)}{stack[-1]}'
            
        return res
