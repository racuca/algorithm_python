def bubblesort(datalist):
    for idx in range(len(datalist) - 1):
        for index in range(1, len(datalist) - idx):
            if datalist[index - 1] > datalist[index]:
                temp = datalist[index - 1]
                datalist[index - 1] = datalist[index]
                datalist[index] = temp
                print("index", index - 1, index, "data 교환", datalist[index - 1], datalist[index])
            else:
                print("index", index - 1, index)
        print("턴 정렬 결과", datalist)

list = [3, 4, 5, 1, 2]
print("정렬 전 =>", list)
bubblesort(list)
print("정렬 결과 =>", list)
