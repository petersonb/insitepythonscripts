infile = open("duplicates.txt")

heilerNums = []
for line in infile:
    line = line.split("|")
    if (len(line) < 3):
        continue
    print(line)
    heilerNums.append(line[2])
for thing in sorted(heilerNums):
    print(thing)
print(len(heilerNums))
infile.close()
