import sys

scores = sys.stdin.readlines()

numbers = [int(i) for i in scores]

totalscoreA = numbers[0]* 3 + numbers[1] * 2 + numbers[2]
totalscoreB = numbers[3]* 3 + numbers[4] * 2 + numbers[5]


if totalscoreA > totalscoreB:
    print("A")
elif totalscoreB > totalscoreA:
    print("B")
else:
    print("T")
