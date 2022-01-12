# 700 Leet code Search in a Binary Search Tree 
#You are given the root of a binary search tree (BST) and an integer val.

#Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def searchBST(self, root, val):
    #     """
    #     :type root: TreeNode
    #     :type val: int
    #     :rtype: TreeNode
    #     """
    #     # Recursive
    #     if not root:
    #         return None
    #     if root.val == val:
    #         return root
    #     elif root.val > val:
    #         return self.searchBST(root.left, val)
    #     else:
    #         return self.searchBST(root.right, val)

    def searchBST(self, root, val):
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return root
