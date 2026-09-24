class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        arr = [0] * n

        for i in range(len(pref)):
            if i:
                arr[i] = pref[i-1] ^ pref[i]
            else:
                arr[i] = pref[i]
        
        return arr