# Write a Python program to read an entire text file.

file = "File_Exercise\sample.txt"
with open(file) as f : # defult in read mode
    content = f.read()
    print(content)     # print the content