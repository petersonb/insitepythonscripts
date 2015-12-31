fileA = open('fileA.txt')
fileB = open('fileB.txt')

# Load in shit from both tables
a = []
b = []

for line in fileA:
    a.append(line.strip())

print('Lines from fileA.txt loaded')

for line in fileB:
    b.append(line.strip())
    
print('Lines from fileB.txt loaded')

fileA.close()
fileB.close()

print('Text files closed')

print('FileA count: {0}'.format(len(a)))
print('FileB count: {0}'.format(len(b)))
      
print('Beginning A to B Comparison')

for item in a:
    if (not b.count(item)):
        print('fileB does not contain item: {0}'.format(item))

print('Beginning B to A Comparison')

for item in b:
    if (not a.count(item)):
        print('fileA does not contain item: {0}'.format(item))
