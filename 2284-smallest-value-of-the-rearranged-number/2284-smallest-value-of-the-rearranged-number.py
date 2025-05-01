class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        if num < 0:
            num = -num 
            numSort = sorted(str(num), reverse=True)
            num = int(''.join(numSort))
            return -num
        else:
            numSort = sorted(str(num))
            count = numSort.count('0')
            if count > 0:
                numSort = numSort[count: count+1] + ['0']*count + numSort[count+1:]
            num = int(''.join(numSort))

            return num
            
