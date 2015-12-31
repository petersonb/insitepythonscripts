infile = open("ticketstatus.txt")
outfile = open("separatedtickets.txt","w")

board = [[],[],[],[],[],[],[],[]]
infilecount = 0
for line in infile:
    if (line.find("BACKLOG") != -1):
        board[0].append(line.strip())
    elif (line.find("TODO") != -1):
        board[1].append(line.strip())
    elif (line.find("QA") != -1):
        board[2].append(line.strip())
    elif (line.find("UAT") != -1):
        board[3].append(line.strip())
    elif (line.find("AWAITINGDEPLOY") != -1):
        board[4].append(line.strip())
    elif (line.find("MERGED") != -1):
        board[5].append(line.strip())
    elif (line.find("DONE") != -1):
        board[6].append(line.strip())
    else:
        board[7].append(line.strip())
    infilecount += 1

print("{0} lines from infile".format(infilecount))

outfilecount = 0
for item in board:
    for ticket in item:
        outfile.write("{0}\n".format(ticket))
        outfilecount += 1
    outfile.write("\n")
    
print("{0} lines from outfile".format(outfilecount))

infile.close()
outfile.close()
