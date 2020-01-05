# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        # 保存头节点
        head = ListNode(None)
        root = head
        while(pHead1 != None and pHead2 != None):
            if pHead1.val < pHead2.val:
                root.next = pHead1
                pHead1 = pHead1.next
            else:
                root.next = pHead2
                pHead2 = pHead2.next
            root = root.next
        # 合并不为空的链表
        if pHead1 == None:
            root.next = pHead2
        if pHead2 == None:
            root.next = pHead1 
        return head.next

if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    listNode2 = ListNode(3)
    listNode2.next = ListNode(4)
    listNode2.next.next = ListNode(6)
    solution = Solution()
    result = solution.Merge(listNode, listNode2)
    print(result)