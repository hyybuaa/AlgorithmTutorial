# -*- coding:utf-8 -*-
# 快排,递归法，时间复杂度为nlog(n)
def quick_sort(array):
    if len(array) == 0:
        return []
    pivot = array[0]
    left = [x for x in array[1:] if x<pivot]
    right = [x for x in array[1:] if x>= pivot]
    quick_sort(left)
    quick_sort(right)
    return left + [pivot] + right

#堆排序，递归法，大顶堆
def head_sort(array, n):
    result = []
    for _ in range(n):
        array = buildMaxHeap(array, len(array))
        result.append(array.pop(0))
    return result

# 构建小顶堆
def buildMaxHeap(heap, n):
    for i in range(n//2-1,-1,-1): # 最后一个非叶子节点
        left = 2*i + 1
        right = 2*i+2
        if left < n and heap[i] > heap[left]:
            heap[i], heap[left] = heap[left], heap[i] # 交换位置
            if (2*left+1 < n and heap[left] > heap[2*left+1]) or (2*left+2 < n and heap[left] > heap[2*left+2]):
                buildMaxHeap(heap, n) # 向下交换位置
        if right < n and heap[i] > heap[right]:
            heap[i], heap[right] = heap[right], heap[i] # 交换位置
            if (2*right+1 < n and heap[right] > heap[2*right+1]) or (2*right+2 < n and heap[right] > heap[2*right+2]):
                buildMaxHeap(heap, n) # 向下交换位置 
    return heap

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        reuslt = head_sort(tinput, k)
        return reuslt

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    solution = Solution()
    result = solution.GetLeastNumbers_Solution(array, 3)
    print(result)