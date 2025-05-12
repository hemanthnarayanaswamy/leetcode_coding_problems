class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arrFreq = Counter(arr)
        arrFreqSort = dict(sorted(arrFreq.items(), key=lambda item:item[1]))
        removeElements = 0
        countElements = 0

        for key in arrFreqSort:
            if removeElements + arrFreqSort[key] <= k:
                removeElements += arrFreqSort[key]
                countElements += 1
            else:
                temp = abs(k - removeElements)
                if arrFreqSort[key] > temp:
                    removeElements += temp
            
            if removeElements == k:
                return abs(countElements - len(arrFreqSort))




            