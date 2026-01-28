class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if m * n != len(original):
            return result
        
        i = 0
        while m:
            result.append(original[i:i+n])
            print(i, i+n, original[i:i+n])
            i += n
            m -= 1
        
        return result
            


        