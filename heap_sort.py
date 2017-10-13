#-*-coding:utf-8-*-
def heap_sort(lst):
    def sift_down(start, end):
        # 最大堆調整
        root = start
        while True:
            child = 2*root+1
            if child > end:
                break
            if child+1 <= end and lst[child] < lst[child+1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break
    # 創建最大堆
    for start in range((len(lst)-2) // 2, -1, -1):
        sift_down(start, len(lst)-1)
    # 堆排序
    for end in range(len(lst)-1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end-1)
    return lst
def main():
    lst = [9,1,7,3,8,2,6,4,5]
    print(heap_sort(lst))

if __name__ == "__main__":
    main()
