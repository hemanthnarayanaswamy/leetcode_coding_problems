class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        result = ""

        for word in words:
            result += word
            if len(result) >=len(s):
                if result == s:
                    return True
                else:
                    return False
        
        return False