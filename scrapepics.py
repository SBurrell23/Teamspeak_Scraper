def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

fileName = 'mike1_channel.txt'
inFile = open(fileName, encoding="utf8")
line = inFile.readline()

outFileName = 'mike1_out.html'
outFile = open(outFileName, 'w')

# Read file line by line, parse the line and write it to an html file.
count = 0;
while line:
    if 'imgur' in line:
        parsedLine = find_between(line,'[URL]','[/URL]')
        parsedLine = '<a target=\"_blank\"href=\"'+parsedLine+'\"><img src=\"'+parsedLine+'\" width=\"150px\" height=\"150px\"></a>'
        outFile.write(parsedLine)
        count+=1
    line = inFile.readline()
    
inFile.close()
outFile.close()

print("All Done! :)")
print(count)
