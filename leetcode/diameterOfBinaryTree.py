# Definition for a binary tree node.
'''
https://leetcode.com/problems/diameter-of-binary-tree/description/

543. Diameter of Binary Tree
Easy
Topics
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode])->int:
        # print(root)
        if root is None: return 0

        left_value = self.diameterOfBinaryTree(root.left)
        right_value = self.diameterOfBinaryTree(root.right)

        max_height = max(left_value, right_value) + 1
        # min_height = min(left_value, right_value) + 1
        # print(max_height)
        # print(height)
        return max_height




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)

    # arr: list[int] = [1,2,3,4,5]

    solution = Solution()
    print(solution.diameterOfBinaryTree(root))

# 1, 2, 4
# 1, 2, 5