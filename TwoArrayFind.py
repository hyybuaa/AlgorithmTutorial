# -*- coding:utf-8 -*-
class Solution():
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        length_row = len(array)
        length_column = len(array[0])-1
        for i in range(length_row):
            if target > array[i][length_column]:
                continue
            elif target == array[i][length_column]:
                return True
            else:
                if target in array[i]:
                    return True
        return False

if __name__ == "__main__":
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    target = 7
    solution = Solution()
    result = solution.Find(target, array)
    print(result)