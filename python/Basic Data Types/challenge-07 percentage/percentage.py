# refereces:
# https://www.sololearn.com/Discuss/1347790/meaning-of-adding-an-asterisk-before-a-variable-in-python 

def getPercentage(query_name,student_marks):
    percentage=None
    if query_name in student_marks:
        query_scores = student_marks[query_name]
        percentage=sum(query_scores)/len(query_scores)
    return percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if getPercentage(query_name,student_marks) != None:
        print("{0:.2f}".format(getPercentage(query_name,student_marks)))
    else:
        print("specify correct student name for query!!")