class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        m = -1 ## we'll store this value that needs to go in the last spot 
        i = len(arr) - 1 # we'll iterate the array from backwards 

        while i >=0:
            temp = arr[i] ## Store current value in the temp 
            # Now we know that the in first iteration lasting from last it'll be last element and last element should be -1 
            arr[i] = m # m is -1 
            # Now before moving to the next element we need to make sure to update the m value with the highest value among temp and m 
            if temp > m:
                m = temp
            i -= 1 # Iterate to next element 
        return arr

### Fastest Solution 
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 1:
            return [-1]
        max_ = max(arr[1:])
        for i in range(0, len(arr)-1, 1):
            if arr[i] != max_:
                arr[i] = max_
            else:
                max_ = max(arr[i+1:])
                arr[i] = max_
        arr[-1] = -1
        return arr
