class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        res = []

        for i in range(n):
            tmp = image[i][::-1]
            for j in range(n):
                if tmp[j]:
                    tmp[j] = 0
                else:
                    tmp[j] = 1
            res.append(tmp)
        
        return res