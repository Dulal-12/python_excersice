# Write a Python program to read first n lines of a file. 

file = "File_Exercise\sample.txt"
n = 4
with open(file) as f:
    for i in range(n):
        content = f.readline()
        print(content)