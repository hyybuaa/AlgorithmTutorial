# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array)==0:
            return None
        value = []
        for i in range(len(array)):
            if i == 0:
                value.append(array[0])
            else:
                tmp = max(array[i], value[i-1]+array[i])
                value.append(tmp)
        result = max(value)
        return result

if __name__ == "__main__":
    array = [1,-2,3,10,-4,7,2,-5]
    solution = Solution()
    result = solution.FindGreatestSumOfSubArray(array)
    print(result)