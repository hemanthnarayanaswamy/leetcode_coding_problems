class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = separator.join(words)
        result = result.split(separator)

        # for word in words:
        #     new_list = word.split(separator)
        #     if new_list:
        #         result += new_list
        
        return [char for char in result if char]
