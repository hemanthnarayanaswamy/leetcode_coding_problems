class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        i = 0 
        while i < len(command):
            if command[i] == '(':
                if command[i+1] == 'a':
                    output += 'al'
                    i += 4
                else:
                    output += 'o'
                    i += 2
            else:
                output += 'G'
                i += 1
        return output