# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, listNode, toDeleteNode):
        if listNode == None or toDeleteNode == None:
            return listNode
        if listNode == toDeleteNode:
            return listNode.next
        if toDeleteNode.next == None:
            while(listNode.next != toDeleteNode):
                listNode = listNode.next
            listNode.next = None
            return listNode
        toDeleteNode.val = toDeleteNode.next.val
        toDeleteNode.next = toDeleteNode.next.next
        return listNode

if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    solution = Solution()
    headNode = ListNode(1)
    headNode.next = listNode.next
    toDeleteNode = listNode.next
    toDeleteNode.next = listNode.next.next
    result = solution.deleteNode(listNode, toDeleteNode)
    print(result)