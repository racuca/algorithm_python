def bubblesort(data):
    for sorted_num in range(len(data)-1):
        for idx in range(len(data)-1-sorted_num):
            if data[idx] > data[idx+1]:
                temp = data[idx]
                data[idx] = data[idx+1]
                data[idx+1] = temp
                print("index", idx, idx+1, "data교환", data[idx], data[idx+1])
            else:
                print("index", idx, idx+1)

l1 = [3, 4, 5, 1, 2]
print("데이터", l1)
bubblesort(l1)
print("정렬 데이터", l1)
