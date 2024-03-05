def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def iparent(id):
    return int(id / 2)

def ileftchild(id):
    return 2*id + 1

def siftdown(a, root, end): # 2, 5
    while ileftchild(root) < end:
        child = ileftchild(root)
        if child+1 < end and a[child] < a[child+1]:
            child = child+1
        if a[root] < a[child]:
            swap(a, root, child)
            print(a, root, child)
            root = child
        else:
            return

def heapify(a, count):
    start = iparent(count-1)+1
    print("heapify start", start)
    while start > 0:
        start = start - 1
        siftdown(a, start, count)

def heapsort(a, count):
    print("heapify", a)
    heapify(a, count)  # 가장 큰 값이 루트에 오도록 힙을 구성
    print("heapify result", a)
    end = count
    while end > 1:
        end = end - 1
        swap(a, end, 0)
        siftdown(a, 0, end)

l = [3, 1, 5, 4, 2]
heapsort(l, 5)
print(l)

l = [3, 5, 8, 4, 6, 1, 9, 7, 2]
heapsort(l, 9)
print(l)