class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        stack = []

        for i in range(len(bits)):
            if stack:
                bit = stack.pop()
                if bit == 0:
                    stack.append(bits[i])
            else:
                stack.append(bits[i])
        
        return len(stack) == 1