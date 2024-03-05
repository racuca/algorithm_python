import math
def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def idxleftchild(p):
    return 2*p + 1

def heapsort(a, count):
    start = math.floor(count/2)
    end = count
    while end > 1:
        if start > 0:
            start -= 1
        else:
            end -= 1
            swap(a, end, 0)
            print("swap", a)
        print("start end : ", start, end)
        root = start
        while idxleftchild(root) < end:
            child = idxleftchild(root)
            # 오른쪽 자식이 있고 더 크다면
            if child+1 < end and a[child] < a[child+1]:
                child += 1
            if a[root] < a[child]:
                swap(a, root, child)
                print("exch", a)
                root = child
            else:
                break

l = [3, 5, 4, 1, 2]
heapsort(l, 5)
print(l)

l = [3, 5, 8, 4, 6, 1, 9, 7, 2]
heapsort(l, 9)
print(l)