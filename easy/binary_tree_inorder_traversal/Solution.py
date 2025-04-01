# from data_structures.TreeNode import TreeNode
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
        
    #     return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = [] # Will store Node values
        stack = [] # will store TreeNodes

        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)

            current = current.right
        
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(6)
    root.left.right.right = TreeNode(7)
    
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(9)

    print(Solution().inorderTraversal(root))