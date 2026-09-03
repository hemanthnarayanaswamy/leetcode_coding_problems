class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        odds = []
        evens = []

        for i in range(n):
            num = nums1[i]
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)
        
        if not odds or not evens:
            return True
        
        min_odd = min(odds)
        min_even = min(evens)
        e = o = True

        for i in range(n):
            num = nums1[i]
            if num % 2 and num - min_odd < 1:
                o = False
            
            if num % 2 == 0 and num - min_odd < 1:
                e = False

        return e or o            


        
