with open("sample.txt") as f:
    content = f.read().lower()
content = content.replace("donkey" , '&*#*#*')
with open("sample.txt" , 'w') as f:
    f.write(content)
    