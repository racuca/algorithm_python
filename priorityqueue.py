class Heap:
    def __init__(self, p, data):
        self.priority = p
        self.data = data

HeapArray = [0]

def getParent(idx):
    return idx // 2

def printheap():
    if len(HeapArray) == 1:
        print("No node")
        return

    for h in HeapArray[1:]:
        print(h.priority, end=", ")
    print()

def insertHeap(priority, data):
    idx = len(HeapArray)

    # 마지막노드에 추가
    newHeap = Heap(priority, data)
    HeapArray.append(newHeap)
    # 부모와 비교하여 교환

    # idx 가 1 보다 작으면 루트노드이므로 비교가 완료되었다.
    while idx > 1:
        p = getParent(idx)
        if HeapArray[p].priority > priority:
            HeapArray[idx] = HeapArray[p]
            idx = getParent(idx)
        else:
            break
    HeapArray[idx] = newHeap
    printheap()

if 1:
    insertHeap(99, "A")
    insertHeap(55, "B")
    insertHeap(60, "C")
    insertHeap(70, "D")
    insertHeap(80, "E")
    insertHeap(50, "D")
    insertHeap(40, "E")
    insertHeap(1, "F")
else:
    insertHeap(1, "A")
    insertHeap(40, "B")
    insertHeap(50, "C")
    insertHeap(80, "D")
    insertHeap(70, "E")
    insertHeap(60, "D")
    insertHeap(55, "E")
    insertHeap(99, "F")


def getChild(idx):
    leftchild = 2 * idx
    rightchild = 2 * idx + 1
    # 자식이 존재하는지 검사
    if leftchild >= len(HeapArray):
        return 0
    if rightchild >= len(HeapArray):
        return leftchild
    # 두 자식 비교
    if HeapArray[leftchild].priority < HeapArray[rightchild].priority:
        return leftchild
    else:
        return rightchild

def deleteHeap():
    lastnode = HeapArray[len(HeapArray)-1]
    HeapArray.remove(lastnode)
    if len(HeapArray) == 1:
        printheap()
        return

    HeapArray[1] = lastnode

    lastnodeidx = 1
    cidx = 1
    while cidx:
        cidx = getChild(lastnodeidx)
        if cidx == 0:
            break
        if lastnode.priority > HeapArray[cidx].priority:
            HeapArray[lastnodeidx] = HeapArray[cidx]
            lastnodeidx = cidx
        else:
            break
    HeapArray[lastnodeidx] = lastnode
    printheap()

deleteHeap()
deleteHeap()
deleteHeap()
deleteHeap()
deleteHeap()
deleteHeap()
deleteHeap()
deleteHeap()
