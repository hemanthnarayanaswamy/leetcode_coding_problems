class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s, len_t = len(s), len(t)

        if len_s != len_t:
            return False 
        
        dict_s, dict_t = {}, {}

        for i in range(len_s):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1
        
        return dict_s == dict_t
        