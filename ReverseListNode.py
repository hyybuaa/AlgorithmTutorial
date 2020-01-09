# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return pHead
        # 初始化前一个节点
        root = None
        while(pHead != None):
            # 下一个节点
            next = pHead.next
            # 当前节点指向前一个节点
            pHead.next = root
            # 当前节点向后走
            root = pHead
            # 传递下一个节点
            pHead = next
        return root



if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    solution = Solution()
    result = solution.ReverseList(listNode)
    print(result)