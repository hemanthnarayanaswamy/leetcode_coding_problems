class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_character(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
            return stack 
        
        return remove_character(s) == remove_character(t)
        