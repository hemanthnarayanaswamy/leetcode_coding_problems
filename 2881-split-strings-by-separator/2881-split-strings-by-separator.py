class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        joinedWords = separator.join(words)
        result = joinedWords.split(separator)
        
        return [char for char in result if char] # remove empty strings
