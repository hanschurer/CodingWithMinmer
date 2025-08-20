#https://leetcode.cn/problems/simplify-path/?envType=problem-list-v2&envId=bmaYUCaj
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split("/"):
            if directory == "..":
                if len(stack) > 0:
                    stack.pop()
            elif directory and directory != ".":
                stack.append(directory)
        return "/" + "/".join(stack)
