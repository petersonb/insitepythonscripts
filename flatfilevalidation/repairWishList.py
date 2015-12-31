filename = input("Enter name of file (include .dat on end) or press enter for default 'in.dat': ")
if filename == "":
    filename = "in.dat"
try:
    infile = open(filename)
except:
    input("\nI did not find '{0}' in this directory.\nPlease make sure you are running this script with '{0}' in the same directory.\nPress enter to end programm unsuccessfully...".format(filename))
    raise

outfilename = "out_{0}".format(filename)
outfile = open(outfilename, "w")
for line in infile:
    outfile.write(line)
infile.close()
outfile.close()
input("\nI have written the result to {0}.\n\nPress enter to end program as success.".format(outfilename))
