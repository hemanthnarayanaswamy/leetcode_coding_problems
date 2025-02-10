class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sList = list(s) # Convert String in List
        stack = []
        for i,char in enumerate(s): ## Tracking Excess ')'
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    sList[i] = "" ## Replace ')' with a empty string 
    ## ['l', 'e', 'e', '(', 't', '(', 'c', ')', 'o', ')', 'd', 'e', '']

        for i in stack:   ## Now whatever if left in stack are the excess ')'
            sList[i] = "" ## mark them as empty strings 
        
        return "".join(sList) ## Join the List 
              
            
        