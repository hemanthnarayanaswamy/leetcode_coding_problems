class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        res = 0

        for num in range(100, 1000, 2):
            needed = Counter([int(d) for d in str(num)])
            valid = all(freq[d] >= needed[d] for d in needed)
            
            if valid:
                res += 1
        
        return res




