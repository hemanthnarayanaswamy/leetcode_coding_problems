class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        nums = [element for row in grid for element in row]
        lenght = len(nums)

        res = [1]*(lenght)

        prefix = 1
        for i in range(lenght):
            res[i] = prefix
            prefix = (prefix * nums[i]) % 12345
        
        postfix = 1
        for i in range((lenght)-1, -1, -1):
            res[i] = (res[i] * postfix) % 12345
            postfix = (postfix * nums[i]) % 12345
        
        return [res[i:i+n] for i in range(0, lenght, n)]
