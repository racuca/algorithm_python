def selectionsort(datalist):
    for idx in range(len(datalist)-1):
        # 최소값 찾기
        min = datalist[idx]
        minindex = idx
        for step in range(idx+1, len(datalist)):
            if min > datalist[step]:
                min = datalist[step]
                minindex = step
        print("찾은 min", min, "위치", minindex)
        datalist[minindex] = datalist[idx]
        datalist[idx] = min
        print("값 교환", min, datalist[minindex])

l1 = [3, 5, 4, 1, 2]
print("정렬 전 =>", l1)
selectionsort(l1)
print("정렬 결과 =>", l1)
