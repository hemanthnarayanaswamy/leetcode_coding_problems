class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        lenword1 = len(word1)
        lenword2 = len(word2)

        for i in range(max(lenword1, lenword2)):
            if i < lenword1:
                result.append(word1[i])
            if i < lenword2:
                result.append(word2[i])
        
        return "".join(result)

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = []
#         i = 0
#         len_word1 = len(word1)
#         len_word2 = len(word2)

#         while i < len_word1 or i < len_word2:
#             if i < len_word1:
#                 result.append(word1[i])
#             if i < len_word2:
#                 result.append(word2[i])
#             i += 1
#         return "".join(result)
            