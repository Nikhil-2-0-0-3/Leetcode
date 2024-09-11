# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        s1,s2=[],[]
        def get_ss(root,s):
            if not root:
                return
            if not root.left and not root.right:
                s.append(root.val)
            else:
                get_ss(root.left,s)
                get_ss(root.right,s)
        get_ss(root1,s1)
        get_ss(root2,s2)
        return(s1==s2)
