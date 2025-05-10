class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ''
        sfreq = Counter(s)

        for char in order:
            result += char * sfreq.get(char, 0)
        
        for char, n in sfreq.items():
            if char not in result:
                result += char * n
        
        return result
     
