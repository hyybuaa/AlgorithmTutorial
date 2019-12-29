# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstruBinaryTree(self, pre, tin):
        node = self.construBinaryTree(pre, 0, len(pre)-1, tin, 0, len(tin)-1)
        return node

    def construBinaryTree(self, pre, ps, pe, tin, ts, te):
        """
        重构二叉树
        :param pre: 前序列表
        :param ps: 前序起点
        :param pe: 前序终点
        :param tin: 中序列表
        :param ts: 中序起点
        :param te: 中序终点
        :return:
        """
        if ps > pe:
            return None
        value = pre[ps]
        # 检查中序的根结点是否一致
        index = ts
        while(ts<=te and tin[index]!=value):
            index += 1
        while(ts>te):
            return None
        node = TreeNode(value)
        # 左子树的节点个数为index-ts+1
        # 右子树的节点个数为te-index+1
        node.left = self.construBinaryTree(pre, ps+1, ps+index-ts,tin, ts, index-1)
        node.right = self.construBinaryTree(pre, ps+index-ts+1, pe, tin, index+1, te)
        return node

if __name__ == "__main__":
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    solution = Solution()
    result = solution.reConstruBinaryTree(pre, tin)
    print(result)