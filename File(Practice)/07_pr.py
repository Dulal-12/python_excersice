content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline().lower()
        if('python' in content):
           print(f'python is line number {i}')
        i += 1 