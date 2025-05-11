class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrFreq = Counter(arr)
        arrFreq = dict(sorted(arrFreq.items(), key=lambda item: item[1], reverse=True))
        n = len(arr)
        answer, counter = 0, 0

        for key, val in arrFreq.items():
            if answer < n // 2:
                answer += val 
                counter += 1
            elif answer > n // 2:
                return counter
        
        return counter 
        
