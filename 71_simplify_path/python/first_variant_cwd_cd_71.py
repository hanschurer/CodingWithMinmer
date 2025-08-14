class Solution:
    def changeDirectory(self, cwd: str, cd: str) -> str:
        if cd == "":
            return cwd
        if cd[0] == "/":
            cwd = ""
        
        stack = [p for p in cwd.split("/") if p]
        for p in cd.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)
        return "/"+"/".join(stack)



if __name__ == "__main__":
    solution = Solution()
    assert solution.changeDirectory("/a/b/c", "/d/./e") == "/d/e"
    assert solution.changeDirectory("", "/d/./e") == "/d/e"
    assert solution.changeDirectory("/a/b/c", "") == "/a/b/c"
    assert solution.changeDirectory("/a/b", ".//c/../../d/f") == "/a/d/f"
    assert solution.changeDirectory("/", "foo") == "/foo"
    assert solution.changeDirectory("/", "foo/bar/././xyz///") == "/foo/bar/xyz"
    assert solution.changeDirectory("/baz", "/bar") == "/bar"
    assert solution.changeDirectory("/foo/bar", "../../../../..") == "/"
    assert solution.changeDirectory("/x/y", "../p/../q") == "/x/q"
    assert solution.changeDirectory("/x/y", "/p/./q") == "/p/q"
    assert solution.changeDirectory("/facebook/anin", "../abc/def") == "/facebook/abc/def"
    assert solution.changeDirectory("/facebook/instagram", "../../../../.") == "/"
