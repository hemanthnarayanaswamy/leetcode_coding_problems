class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        prefix = 0
        C = []

        for a, b in zip(A, B):
            freq[a] += 1
            freq[b] += 1

            if a != b:
                if freq[a] == 2 and freq[b] == 2:
                    prefix += 2
                elif freq[a] == 2 or freq[b] == 2:
                    prefix += 1
            else:
                if freq[a] == 2:
                    prefix += 1
            
            C.append(prefix)


        return C