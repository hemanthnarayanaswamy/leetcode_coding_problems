class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        arr = [0] * n

        for i, p in enumerate(pref):
            if i:
                arr[i] = pref[i-1] ^ p
            else:
                arr[i] = p
        
        return arr