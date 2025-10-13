class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        prev_sig = None
        
        for word in words:
            sig = ''.join(sorted(word))
            if stack and prev_sig == sig:
                    continue
           
            stack.append(word)
            prev_sig = sig
        
        return stack
