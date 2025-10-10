class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        print(path)

        for dir in path:
            if dir and dir != '.':
                if stack and dir == '..':
                    stack.pop()
                elif dir != '..':
                    stack.append(dir)
        
        return '/'+'/'.join(stack)