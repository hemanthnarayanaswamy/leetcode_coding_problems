class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = []
        
        # Process each diagonal
        for d in range(m + n - 1):
            diagonal = []
            
            # Collect elements in current diagonal
            for i in range(m):
                j = d - i
                if 0 <= j < n:
                    diagonal.append(mat[i][j])
            
            # Add in correct direction
            if d % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)
        
        return result