# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        isSameTree = False
        pArr = []
        qArr = []
        self.helper(p, pArr)
        self.helper2(q, qArr)
        if pArr == qArr:
            isSameTree = True
        return isSameTree

    def helper(self, p, pArr):
        if p == None:
            pArr.append("null")
        if p:
            pArr.append(p.val)
            self.helper(p.left, pArr)
            self.helper(p.right, pArr)

    def helper2(self, q, qArr):
        if q == None:
            qArr.append("null")
        if q:
            qArr.append(q.val)
            self.helper(q.left, qArr)
            self.helper(q.right, qArr)