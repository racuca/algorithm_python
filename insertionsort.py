def insertionsort(data):
    for i in range(1, len(data)):
        idx = i - 1
        temp = data[i]
        while idx>=0 and data[idx] > temp:
            data[idx+1] = data[idx] # 데이터를 하나 뒤로 밀고
            print("데이터 이동 {} : {}->{}".format(data[idx], idx, idx+1))
            idx-=1                  # 인덱스 감소
        data[idx+1] = temp
        print("데이터 삽입", idx+1, temp)

l1 = [3, 5, 4, 1, 2]
print("정렬 전:", l1)
insertionsort(l1)
print("정렬 결과:", l1)
