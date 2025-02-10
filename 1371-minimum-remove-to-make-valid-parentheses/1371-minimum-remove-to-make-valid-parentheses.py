class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] ## To store the Index of "(" & ")" 
        s= list(s) ## String is immutable so we need list 

        for i in range(len(s)): ## We are marking excess closing ")" as a empty string 
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop() 
                else:
                    s[i] = ""
        
        while stack: ## Now we remove any excess opening "("
                s[stack.pop()] = ""
        
        return ''.join(s)
              
            
        