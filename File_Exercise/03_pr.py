# Write a Python program to append text to a file and display the text.

file = "File_Exercise\sample.txt"
with open(file , 'a') as f:
    f.write("City University\n")
with open(file) as f:
    content = f.read()
    print(content)