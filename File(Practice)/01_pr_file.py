with open("poem.txt") as f:
    content = f.read()
    # print(content)
if "twinkle" in content:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
    