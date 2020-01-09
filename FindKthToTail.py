# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k == None:
            return head
        if k==0:
            return None
        listNode = head
        length = 0
        while(head.next!=None):
            head = head.next
            if length>=k-1:
                listNode = listNode.next
            length += 1
        if length>=k-1:
            return listNode
        else:
            return None

if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    k = 4
    solution = Solution()
    result = solution.FindKthToTail(listNode, k)
    print(result)