# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Inorder --> left - root - right

# recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def traverse(root):
            if root:
                traverse(root.left)
                output.append(root.val)
                traverse(root.right)
        
        traverse(root)
        return output

#iterative soluton
class Solution_iter:
    def inorderTraversal(self):
        output = []
        stack = []

        if not root:
            return output
        while root or root.left or root.right:
            if root.left:
                stack.append(root)
                root = root.left
            else:
                output.append(root.val)
                if root.right:
                    root = root.right
                else:
                    if stack:
                        root = stack.pop()
                        root.left = None
                    else:
                        return output