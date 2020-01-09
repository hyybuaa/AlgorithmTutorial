# -*- coding:utf-8 -*-
# 归并排序
count = 0
def merge_sort(array):
     if len(array) <= 1:
         return array
     mid = len(array) // 2
     left = array[:mid]
     right = array[mid:]
     # 继续分治, 得到排好序的数组
     left = merge_sort(left)
     right = merge_sort(right)
     return merge(left, right)

def merge(left, right):
    global count
    l=r=0
    result = []
    while(l<len(left) and r<len(right)):
        # 添加较小值
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            count += len(left) - l
    # 直接合并未必较的数组
    result += left[l:]
    result += right[r:]
    return result

class Solution:
    def InversePairs(self, data):
        global count
        _ = merge_sort(data)
        return count%1000000007

if __name__ == "__main__":
    array = [1,-2,3,10,-4,7,2,-5]
    solution = Solution()
    result = solution.InversePairs(array)
    print(result)