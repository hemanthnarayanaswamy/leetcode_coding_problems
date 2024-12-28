class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for i in range(len(strs[0])): # Taking the first letter as reference # Taking first words letters as reference to compare it with all other letters 
            for str in strs: #  Now iterating through each letter and checking if our refercnce letter is same as the one in the letters 
                if i == len(str) or strs[0][i] != str[i]:
                    # if the i is out of range because we are using first letter it can be large or small compared to other letters if its large than we'll encounter the out of bound error so that condition and checking the letter is same or not.
                    return result 
            result += strs[0][i]
        return result
    
