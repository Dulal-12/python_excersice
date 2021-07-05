#Use open function to read the content of a file !
with open("sample.txt") as f: # By default, the mode is r
    # data = f.read()
    data = f.read(10) #first 10 character from the file.
    print(data)