# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []

    def push(self, node):
        # write code here
        self.__stack1.append(node)
        if self.__stack2 == [] or self.__stack2[-1] > node:
            self.__stack2.append(node)
        else:
            self.__stack2.append(self.__stack2[-1])
    def pop(self):
        # write code here
        self.__stack2.pop()
        return self.__stack1.pop()
    def top(self):
        # write code here
        return self.__stack1[-1]
    def min(self):
        # write code here
        return self.__stack2[-1]