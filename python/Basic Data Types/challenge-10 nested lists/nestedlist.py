if __name__ == '__main__':
    arr = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append(list([name, score]))
        scores.append(arr[_][1])
    
    # sort list by score in ascending order
    arr.sort(key=lambda x: x[1])
    lowScore = arr[0][1]

    #print("Low Score = {}".format(lowScore))
    for i in range(len(arr)):
        if lowScore >= arr[i][1]:
            continue
        secondLowScore=arr[i][1]
        break
    
    #print("Second Low Score = {}".format(secondLowScore))

    # sort list by name in ascending order
    arr.sort(key=lambda x: x[0])
    for i in range(len(arr)):
        if arr[i][1] == secondLowScore:
            print(arr[i][0])
