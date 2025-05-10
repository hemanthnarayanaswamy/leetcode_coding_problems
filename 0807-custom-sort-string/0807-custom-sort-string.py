class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = []
        sfreq = Counter(s)

        for char in order:
            if char in sfreq:
                result.append(char * sfreq[char])
        
        for char, n in sfreq.items():
            if char not in order:
                result.append(char * n)
        
        return ''.join(result)
     
