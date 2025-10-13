class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(s1, s2):
            if Counter(s1) == Counter(s2):
                return True
            return False
        
        stack = []
        
        for i in range(len(words)):
            if stack:
                if not isAnagram(stack[-1], words[i]):
                    stack.append(words[i])
            else:
                stack.append(words[i])
        
        return stack
