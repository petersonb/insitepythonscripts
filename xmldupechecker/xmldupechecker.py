import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('in.xml').getroot()
outfile = open('out.txt', 'w')

vals = []
duplicates = []
for item in e.findall('_x0031_Category/Category'):
    text = item.text
    vals.append(text)
    if (vals.count(text) > 1):
        if (text == None):
            text = "None"
        duplicates.append(text)

for item in sorted(duplicates):
    print(item)
    outfile.write("{0}\n".format(item))

outfile.close()
