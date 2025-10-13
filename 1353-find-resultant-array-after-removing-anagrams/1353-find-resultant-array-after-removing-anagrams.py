class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        
        for word in words:
            if stack and Counter(stack[-1]) == Counter(word):
                    continue
           
            stack.append(word)
        
        return stack
