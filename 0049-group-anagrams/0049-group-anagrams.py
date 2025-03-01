class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            result[sorted_str] = result.get(sorted_str, []) + [string]
                
        return list(result.values())
            