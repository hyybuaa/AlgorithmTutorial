# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        tmp = []
        result = []
        while(listNode):
            tmp.append(listNode.val)
            listNode = listNode.next
        while(tmp):
            result.append(tmp.pop())
        return result

if __name__ == "__main__":
    listNode = ListNode(1)
    listNode.next = ListNode(2)
    listNode.next.next = ListNode(3)
    solution = Solution()
    result = solution.printListFromTailToHead(listNode)
    print(result)
