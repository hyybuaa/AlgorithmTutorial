# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        p2 = p3 = p5 = 0
        result = [0] * index
        result[0] = 1
        for i in range(1, index):
            tmp = min(result[p2]*2, min(result[p3]*3, result[p5]*5))
            result[i] = tmp
            # 为了防止重复，需要计算三个值参与计算的情况
            if result[i] == result[p2]*2:
                p2 += 1
            if result[i] == result[p3]*3:
                p3 += 1
            if result[i] == result[p5]*5:
                p5 += 1
        return result[-1]

if __name__ == "__main__":
    n = 1500
    solution = Solution()
    result = solution.GetUglyNumber_Solution(n)
    print(result)