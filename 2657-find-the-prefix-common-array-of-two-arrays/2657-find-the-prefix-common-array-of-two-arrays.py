class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        prefix = 0

        c = []

        for a, b in zip(A, B):
            freq[a] += 1
            freq[b] += 1

            if a != b:
                if freq[a] == 2:
                    prefix += 1
                
                if freq[b] == 2:
                    prefix += 1
            else:
                if freq[a] == 2:
                    prefix += 1
            
            c.append(prefix)


        return c