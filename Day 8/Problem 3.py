class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        leftH = self.maxDepth(root.left)
        rightH = self.maxDepth(root.right)
        return (max(leftH, rightH) + 1)