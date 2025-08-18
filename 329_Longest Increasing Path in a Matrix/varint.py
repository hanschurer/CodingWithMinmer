 #需要求从指定点出发的最长递增路径。class Solution:
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    m, n = len(matrix), len(matrix[0])
    res = 0
    @cache
    def dfs(r,c):
        best =1
        for dr, dc in directions:
            nr , nc = dr+r, dc +c
            if nr in range(m) and nc in range(n) and matrix[nr][nc] > matrix[r][c]:
                best= max(best, dfs(nr,nc)+1)
        return best
    
    for r in range(m):
        for c in range(n):
            res = max(res, dfs(r,c))
    return res