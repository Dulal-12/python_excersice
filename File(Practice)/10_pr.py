import os
old = "sample.txt"
new = "dulal.txt"

with open(old, "rt") as f:
    content = f.read()
with open(new, "wt") as f:
    f.write(content)
os.remove(old)