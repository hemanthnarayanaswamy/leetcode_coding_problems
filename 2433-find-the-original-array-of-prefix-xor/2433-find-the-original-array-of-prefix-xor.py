class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = []

        for i in range(len(pref)):
            if i:
                arr.append(pref[i-1] ^ pref[i])
            else:
                arr.append(pref[i])
        
        return arr