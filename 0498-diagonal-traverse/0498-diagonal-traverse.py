def findDiagonalOrder(mat):
    diagonalMat = defaultdict(list)
    res = []

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            diagonalMat[i+j].append(mat[i][j])
    
    # diagonalMat = dict(sorted(diagonalMat.items(), key=lambda item: item[0]))

    for i, val in diagonalMat.items():
        if i % 2:
            res.extend(val)
        else:
            res.extend(val[::-1])

    return res