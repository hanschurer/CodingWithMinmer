from typing import Optional, List


# Given the root of a N-ary tree, return the length of the diameter of the tree.
# The diameter of an N-ary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# An N-ary tree is a tree where each node can have more than two children.
# Example 1:
# Input: root = [1, null, 2,3, null, 4,5,6, null, 7,8,9, null]
# Output: 4
# Explanation: 3 is the length of the path 
# [7,6,2,1,31, [8,6,2,1,3] or [9,6,2,1,3]. Note the input is represented in level order traversal, each group of children is separated by the null value.


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def longest_path(node: 'Node'):
            if node is None:
                return 0

            max_height = 0
            second_max_height = 0
            for child in node.children:
                height = longest_path(child)
                if height > max_height:
                    second_max_height = max_height
                    max_height = height
                elif height > second_max_height:
                    second_max_height = height
            nonlocal diameter
            diameter = max(diameter, max_height + second_max_height)
            return max_height + 1

        longest_path(root)

        return diameter