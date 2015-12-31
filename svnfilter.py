infile = open("rawcommits.txt")
outfile = open("filtereddata.txt","w")
ticketfile = open("ticketdata.txt","w")
ticketonly = open("ticketonly.txt","w")

tickets = []

def include(line):
    keywords = ["Author","Date","TOH","Revision","----"]
    for item in keywords:
        if line.find(item) != -1:
            if item == "TOH":
                tickets.append(line.strip())
            return True
    return False
        

for line in infile:
    if include(line):
        outfile.write("{0}\n".format(line.strip()))
        
tickets = sorted(tickets)
for item in tickets:
    ticketfile.write("{0}\n".format(item))

ticketnumbers = []
for item in tickets:
    ticketNumber = item.split()[0]
    if ticketnumbers.count(ticketNumber) < 1:
        ticketnumbers.append(ticketNumber)
        ticketonly.write("{0}\n".format(ticketNumber))

print("project = TOH AND key in ({0}) ORDER BY summary ASC".format(",".join(ticketnumbers)))


infile.close()
outfile.close()
ticketfile.close()
ticketonly.close()

