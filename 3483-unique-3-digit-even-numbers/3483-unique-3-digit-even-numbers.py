class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        even = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i in (j, k) or j in (i, k) or digits[i] == 0 or digits[k] % 2:
                        continue

                    num = 100*digits[i]+10*digits[j]+digits[k]
                    even.add(num)
        
        return len(even)


