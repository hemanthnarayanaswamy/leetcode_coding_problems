class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        stack = []

        for i in range(len(bits)):
            if stack:
                if stack[-1]:
                    stack.pop()
                else:
                    stack.pop()
                    stack.append(bits[i])
            else:
                stack.append(bits[i])
        
        return len(stack) == 1