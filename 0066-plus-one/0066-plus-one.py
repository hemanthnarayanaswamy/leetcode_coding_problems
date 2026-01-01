class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(d) for d in digits])
        num = int(num) + 1
        
        num = list(str(num))

        return [int(d) for d in num]