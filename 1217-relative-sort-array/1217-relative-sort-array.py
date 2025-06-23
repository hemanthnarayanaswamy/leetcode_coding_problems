class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1Freq = Counter(arr1)
        result = []
        extraNum = []

        for num in arr2:
            temp = [num] * arr1Freq[num]
            result += temp 
        
        for num in arr1Freq:
            if num not in result:
                temp = [num] * arr1Freq[num]
                extraNum += temp
        
        extraNum.sort()
        
        return result + extraNum
        
