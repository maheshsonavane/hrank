if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    tempList = list(arr)
    tempList.sort(reverse=True)
    highScore = tempList[0]
    for i in range(n):
        if highScore <= tempList[i]:
            continue
        print(tempList[i])
        break