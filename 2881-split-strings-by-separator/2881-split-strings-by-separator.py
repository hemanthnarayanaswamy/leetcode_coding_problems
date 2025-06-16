class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # result = separator.join(words)
        # result = result.split(separator)
        result = []

        for word in words:
            result += word.split(separator)
        
        return [char for char in result if char]
