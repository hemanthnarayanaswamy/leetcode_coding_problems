class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for token in path.split('/'):
            if token == '' or token == '.':
                continue
            if token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
                
        return '/' + '/'.join(stack)