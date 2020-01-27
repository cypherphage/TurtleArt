# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Preorder -->  root - left - right

# recursive solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []

        def traverse(root):
            if root:
                output.append(root.val)
                traverse(root.left)            
                traverse(root.right)

        traverse(root)
        return output

#iterative solution
class Solution_iter:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        stack = []

        if not root:
            return output
        while root or root.left or root.right:
            output.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                root = root.left
            else:
                if stack:
                    root = stack.pop()
                else:
                    return output    
