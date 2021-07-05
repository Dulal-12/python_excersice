with open("sample.txt") as f:
    content = f.read()
with open("this.txt" , 'wt') as f:
    f.write(content)