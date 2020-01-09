# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        i = 0
        length = len(array)
        while(i<length):
            while(i<length and array[i]%2!=0): # 找到偶数
                i += 1
            j = i + 1
            while(j < length and array[j]%2==0 ): # 找到奇数
                j += 1
            if j < length:
                tmp = array[j]
                while(j>i): # i到j-1 元素后移一位
                    array[j] = array[j-1]
                    j -= 1
                array[i] = tmp
            i += 1
        return array


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    solution = Solution()
    result = solution.reOrderArray(array)
    print(result)


