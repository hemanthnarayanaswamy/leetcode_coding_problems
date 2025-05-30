class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrFreq = Counter(arr)
        valueFreq = sorted(arrFreq.values(), reverse=True)
        nhalf = len(arr) // 2
        answer, counter = 0, 0

        for val in valueFreq:
            answer += val 
            counter += 1
            if answer >= nhalf:
                break
        
        return counter 
        
