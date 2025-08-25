class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalMat = defaultdict(list)
    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonalMat[i+j].append(mat[i][j])
        
        result = []
        for diagonal_sum in sorted(diagonalMat.keys()):  # Ensure order
            if diagonal_sum % 2:
                result.extend(diagonalMat[diagonal_sum])
            else:
                result.extend(diagonalMat[diagonal_sum][::-1])
        
        return result