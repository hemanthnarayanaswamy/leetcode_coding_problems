
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arrFreq = Counter(arr)

        for key in arrFreq: 
            cond1, cond2, cond3 =  key * 2, key // 2, key % 2
            if cond1 == key or cond2 == key:
                if arrFreq[key] > 1:
                    return True
                else:
                    continue 

            if cond1 in arrFreq:
                return True
            
            if cond3 == 0 and cond2 in arrFreq:
                return True
        
        return False