infile = open("optoutemails.txt")
outfile = open("out.txt", "w")

first = True
optString = ""
count = 0
for line in infile:
    count += 1
    if first:
        first = False
        optString += "'{0}'".format("''''".join(line.strip().split("'")))
    optString += ",'{0}'".format("''''".join(line.strip().split("'")))
outfile.write(optString)
infile.close()
outfile.close()

input('Final count was {0} >>'.format(count))
