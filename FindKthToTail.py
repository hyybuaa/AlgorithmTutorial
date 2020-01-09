# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findKthToTail(self, head, k):
        if k<0:
            return None
        if head == None:
            return head
        length = 0
        listNode = head
        tmp = None
        while(listNode.next!= None):
            length += 1
            if length>=k:
                tmp = head
                head = head.next
            listNode = listNode.next

        if listNode.next == None:
            if length < k:
                return None
            else:
                return tmp.next


if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    solution = Solution()
    K= 4
    result = solution.findKthToTail(listNode, K)
    print(result)