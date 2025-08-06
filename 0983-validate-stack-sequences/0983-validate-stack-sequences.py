class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        for n in pushed:
            stack.append(n)
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return False if stack else True

            