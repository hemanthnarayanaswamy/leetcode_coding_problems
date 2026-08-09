class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0

        for i in range(n+1):
            if len(set(bin(i)[2:])) == 1:
                count += 1

        return count
