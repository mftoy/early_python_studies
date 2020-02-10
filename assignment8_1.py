fname = input("Enter file name: ")
fh = open(fname)
lst = list()
alst = list()
for line in fh:
    alst = line.split()
    for i in range(len(alst)):
        if not alst[i] in lst:
            lst.append(alst[i])
            print(lst)

lst.sort()
print(lst)
