# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        output = True
        if root:
            queue.append(root)
        else:
            return True
        
        while root.left or root.right or queue:
            temp = []
            count = len(queue)
            while count > 0:
                root = queue.pop()
                count = count - 1
                if root.left:
                    queue.insert(0,root.left)
                    temp.insert(0,root.left.val)
                else:
                    temp.insert(0,None)
                if root.right:
                    queue.insert(0,root.right)
                    temp.insert(0,root.right.val)
                else:
                    temp.insert(0,None)
            count_1 = len(temp)
            if temp[:count_1//2] != temp[count_1//2:][::-1]:
                return False
            
        return output