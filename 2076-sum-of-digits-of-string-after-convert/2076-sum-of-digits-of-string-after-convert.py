class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = []
        # result = ''
        for char in s:
            result.append(str(ord(char)-96))
            # result += str(ord(char)-96)
        
        result = ''.join(result)

        for _ in range(k):
            compute_sum = sum(int(i) for i in result)
            result = str(compute_sum)

        return compute_sum
        