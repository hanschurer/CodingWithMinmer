def flatten(root):
    head = None

    def dfs(root):
        if not root: return 
        nonlocal head

        dfs(root.right)
        dfs(root.left)

        root.left = None
        root.right = head
        head = root 

    return dfs(root)
        