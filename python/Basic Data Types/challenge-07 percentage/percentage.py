# refereces:
# https://www.sololearn.com/Discuss/1347790/meaning-of-adding-an-asterisk-before-a-variable-in-python 

def getPercentage(student_name,student_marks):
    if student_name in student_marks:
        total = 0
        subjectCount = len(student_marks[student_name])
        for mark in student_marks[student_name]:
            total += mark
    return total/subjectCount


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(getPercentage(query_name,student_marks)))