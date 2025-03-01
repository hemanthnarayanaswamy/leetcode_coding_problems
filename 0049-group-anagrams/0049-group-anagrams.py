class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            temp = []
            for c in string:
                temp.append(c)
            temp.sort()
            sorted_str = ''.join(temp)
            if sorted_str in result:
                result[sorted_str] += [string]
            else:
                result[sorted_str] = [string]
                
        return list(result.values())
        