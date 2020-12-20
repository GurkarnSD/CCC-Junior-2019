import sys
totalvalues = []
values = sys.stdin.read().splitlines()

for i in range(1,int(values[0])+1):
    totalvalues.append(values[i].split(' '))

for i in totalvalues:
    print(i[1]*int(i[0]))


