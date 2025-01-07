class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 1:
            return [-1]

        max_ = max(arr[1:])

        for i in range(0,len(arr)-1, 1):
            if arr[i] != max_:
                arr[i] = max_
            else:
                max_ = max(arr[i+1:])
                arr[i] = max_
        arr[-1] = -1
        return arr
