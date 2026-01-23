class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        q, r = divmod(total, 3)
    
        if r:
            return False

        tmp = count = 0
        for num in arr:
            tmp += num

            if tmp == q:
                tmp = 0
                count += 1
            
            if count == 3:
                return True
        
        return False
