def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])
    res = []
    diagnoal = [[]for _ in range(m+n-1)]
    for r in range(m):
        for c in range(n):
            diagnoal[r+c].append(mat[r][c])

    for i in range(len(diagnoal)):
        if i %2 == 0:
            res.extend(diagnoal[i][::-1])
        else:
            res.extend(diagnoal[i])
    return res