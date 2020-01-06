# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == None or len(sequence) == 0:
            return False
        start = 0
        end = len(sequence) - 1
        return self.SquenceOfBST(sequence, start, end)
    
    def SquenceOfBST(self, sequence, start, end):
        if start >= end:
            return True
        index = start
        # 找到第一个大于根节点的数，index-1为左子树，index到end-1为右子树
        # index<end-1, 不能搜索到end，end为根结点可能会出错
        while(index<end-1 and sequence[index] < sequence[end]):
            index += 1
        right = index
        # 右子树都大于根节点，index 等于end
        while(index < end-1 and sequence[index] > sequence[end]):
            index += 1
        if index != end-1:
            return False
        return self.SquenceOfBST(sequence, start, right-1) and self.SquenceOfBST(sequence, right, end-1)

if __name__ == "__main__":
    sequence = [4,8,6,12,16,14,10]
    solution = Solution()
    result = solution.VerifySquenceOfBST(sequence)
    print(result)