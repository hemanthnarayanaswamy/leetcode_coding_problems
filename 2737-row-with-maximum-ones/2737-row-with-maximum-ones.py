class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx, counter = -1, -1

        for i in range(len(mat)):
            x = mat[i].count(1)
            if x > counter:
                counter = x
                idx = i
            
        return [idx, counter]


