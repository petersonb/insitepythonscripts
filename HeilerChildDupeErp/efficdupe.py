import csv


infile = open("in.dat", encoding="utf8")
outfile = open("out.txt", "w")

header = infile.readline()
index = 0
for item in header.split("|"):
    print("{0} {1}".format(index, item))
    index += 1
colcheck = eval(input("What would you like to check for dupes?: "))
expectedLen = colcheck + 1

erpNos = []
with infile as appcsvfile:
    infileReader = csv.reader(appcsvfile, delimiter='|', quotechar='"')
    for row in infileReader:
        erpno = row[colcheck]
        itemCount = erpNos.count(erpno)
        if (itemCount > 0 ):
            print("{0} {1}".format(itemCount, "|".join(row)))
            erpNos.append(erpno)
            outfile.write("{0} {1}".format(itemCount, "|".join(row)))
            outfile.write("\n---\n")
        else:
            erpNos.append(erpno)

print('done')
infile.close()
outfile.close()
