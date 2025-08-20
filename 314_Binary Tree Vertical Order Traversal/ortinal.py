class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    res = []
    min_col = max_col = 0
    q = deque([(root, 0)])
    ct = defaultdict(list)
    while q:
        node, col = q.popleft()

        if node:
            ct[col].append(node.val)
            min_col =min(min_col, col)
            max_col = max(max_col, col)

            q.append((node.left, col-1))
            q.append((node.right, col+1))
    for i in range(min_col, max_col+1):
        res.append(ct[i])
    return res