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

# 归并排序
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    # 继续分治
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
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
    # 直接合并未必较的数组
    result += left[l:]
    result += right[r:]
    return result

#堆排序，递归法，大顶堆
def head_sort(array, n):
    result = []
    for _ in range(n):
        array = buildMaxHeap(array, len(array))
        result.append(array.pop(0))
    return result

# 构建大顶堆
def buildMaxHeap(heap, n):
    for i in range(n//2-1,-1,-1): # 最后一个非叶子节点
        left = 2*i + 1
        right = 2*i+2
        if left < n and heap[i] < heap[left]:
            heap[i], heap[left] = heap[left], heap[i] # 交换位置
            if (2*left+1 < n and heap[left] < heap[2*left+1]) or (2*left+2 < n and heap[left] < heap[2*left+2]):
                buildMaxHeap(heap, n) # 向下交换位置
        if right < n and heap[i] < heap[right]:
            heap[i], heap[right] = heap[right], heap[i] # 交换位置
            if (2*right+1 < n and heap[right] < heap[2*right+1]) or (2*right+2 < n and heap[right] < heap[2*right+2]):
                buildMaxHeap(heap, n) # 向下交换位置 
    return heap

if __name__ == "__main__":
    heap = [7, 3, 8, 5, 4, 1]
    # result = head_sort(heap, 6)
    result_merge = merge_sort(heap)
    # print(result)
    print(result_merge)