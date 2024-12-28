class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in range(len(strs[0])): # Taking the first letter as reference 
            for str in strs:
                if i == len(str) or strs[0][i] != str[i]:
                    return result 
            result += strs[0][i]
        return result