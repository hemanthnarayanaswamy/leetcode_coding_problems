class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def remove_character(string):
            stack = []
            for char in string:
                if stack and char == '#':
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack 
        
        return remove_character(s) == remove_character(t)
        