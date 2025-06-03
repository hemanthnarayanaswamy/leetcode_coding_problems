class Solution:
    def interpret(self, command: str) -> str:
        output = []

        i = 0 

        while i < len(command):
            if command[i] == '(':
                if command[i+1] == ')':
                    output.append('o')
                    i += 2
                else:
                    output.append('al')
                    i += 4
            else:
                output.append('G')
                i += 1
        
        return ''.join(output)