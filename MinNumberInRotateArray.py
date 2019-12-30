# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray)-1
        mid = left
        while(rotateArray[left]>=rotateArray[right]):
            if (right - left) == 1:
                return min(rotateArray[left], rotateArray[right])
            mid = int(left + (right - left)/2)
            # mid 在后段排序中
            if rotateArray[mid] <= rotateArray[right]:
                right = mid
            # mid在前段排序中
            elif rotateArray[mid] >= rotateArray[left]:
                left = mid
        return rotateArray[mid]


if __name__ == "__main__":
    array = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    solution = Solution()
    result = solution.minNumberInRotateArray(array)
    print(result)