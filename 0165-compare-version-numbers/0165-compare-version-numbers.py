class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        n1,n2 = len(v1), len(v2)

        if n1 > n2:
            v2 = v2 + [0]*(n1-n2)
        elif n1 < n2:
            v1 = v1 + [0]*(n2-n1)

        for i in range(max(n1, n2)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        
        return 0
            