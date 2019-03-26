def printLines(a,b):
    print(a+b)
    print(a-b)
    print(a*b)

# to understand the use of __name__ please refer https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    printLines(a,b)    