def add(n1 , n2):
    if n1 == None or n1 == "":
        return "Invalid Operation"
    elif n2 == None or n2 == "":
         return "Invalid Operation"
    else:
        return str(int(n1) + int(n2))
a = add("20" , "39")
print(type(a))