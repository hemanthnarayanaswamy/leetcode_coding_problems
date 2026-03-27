class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        r = k % n
        smat = copy.deepcopy(mat)
        print(r)

        if r == 0:
            return True
        
        while r:
            for i in range(len(smat)):
                if i % 2 == 0:
                    smat[i] = smat[i][1:] + smat[i][:1]
                else:
                    smat[i] = smat[i][-1:] + smat[i][:n-1] 
                print(smat)  
            r -= 1
        print(smat, mat)
        if smat == mat:
            return True
        else:
            return False

