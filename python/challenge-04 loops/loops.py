def printSquareNonNegative(N):
    validRange = range(N)
    for n in validRange:
        print(n**2)

# to understand the use of __name__ please refer https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == '__main__':
    N = int(input())
    printSquareNonNegative(N)