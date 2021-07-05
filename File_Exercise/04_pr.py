# Write a Python program to read last n lines of a file.

file = "File_Exercise\sample.txt"

content = True
i = 0
n = 2
    
with open(file) as f:
    while content:
         content = f.readline()
         if content != "":
             i += 1
# print(i)
lastN = i - n
print(lastN)
with open(file) as f:
    for j in range(i+1):
        if j > lastN : 
            print(f.readline())
            