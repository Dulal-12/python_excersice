file = "File_Exercise\sample.txt"
strList = []
content = True

with open(file) as f:
    while content:
        content = f.readline()
        print(content)
        strList.append(content)
        
print(strList)