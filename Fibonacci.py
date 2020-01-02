# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # 利用动态规划算法
        if n<=0:
            return 0
        array = [0]*n
        if n==1 or n==2:
            return 1
        array[0] = 1
        array[1] = 1
        for i in range(3, n+1):
            array[i-1] = array[i-3] + array[i-2]
        return array[n-1]




if __name__ == "__main__":
    n = 5
    solution = Solution()
    result = solution.Fibonacci(n)
    print(result)