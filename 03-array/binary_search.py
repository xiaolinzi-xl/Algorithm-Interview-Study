
def binarySearch(arr, target):
    # 在[l,r]的范围里寻找target
    l, r = 0, len(arr) - 1
    # 当 l = r 时，区间[l,r]依然是有效的
    while l <= r:
        # mid = (l + r) // 2
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1  # target在[mid+1,r]中
        else:
            r = mid - 1  # target在[l,mid-1]中
    return -1


'''
循环不变量的理解
'''


def main():
    n = 1000000
    arr = [i for i in range(0, n)]

    target = 999

    res = binarySearch(arr, target)
    print(res)


if __name__ == '__main__':
    main()
