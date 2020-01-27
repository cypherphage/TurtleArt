# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Postorder --> left right root

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def traverse(root):
            if root:
                traverse(root.left)
                traverse(root.right)
                output.append(root.val)
        
        traverse(root)
        return output

class Solution_iter:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []

        