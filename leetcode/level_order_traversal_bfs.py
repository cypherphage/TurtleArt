# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        queue = []
        
        if not root:
            return output
        queue.insert(0,root)
        output.append([root.val])
        
        while root.left or root.right or queue:
            count = len(queue)
            out_temp = []
            while count > 0:
                root = queue.pop()
                count = count - 1
                if root.left:
                    queue.insert(0,root.left)
                    out_temp.append(root.left.val)
                if root.right:
                    queue.insert(0,root.right)
                    out_temp.append(root.right.val) 
            if out_temp:
                output.append(out_temp)
        return outpu