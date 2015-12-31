firstfile = input("FirstFile: ")
secondfile = input("SecondFile: ")

a = open("{0}.txt".format(firstfile))
b = open("{0}.txt".format(secondfile))

alines = []
blines = []
for line in a:
    alines.append(line.strip())

for line in b:
    blines.append(line.strip())

for line in alines:
    if (blines.count(line) < 1):
        print(line)
print('split')
for line in blines:
    if (alines.count(line) < 1):
        print(line)

a.close()
b.close()
