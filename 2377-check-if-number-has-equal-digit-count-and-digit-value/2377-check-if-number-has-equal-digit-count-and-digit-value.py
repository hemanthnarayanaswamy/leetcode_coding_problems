class Solution:
    def digitCount(self, num: str) -> bool:
        numFreq = Counter(num)

        for i, n in enumerate(num):
            if numFreq.get(str(i), 0) != int(n):
                return False
        
        return True
