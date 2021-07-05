def valid(txt):
    return (len(txt) == 6 or len(txt) == 4) and txt.isdigit() == True and txt.isspace() == False

print(valid(" 1234"))

#txt.isspace()---> string have any space or not.
#if space --> True else ----> False
#txt.isdigit() ----> check alldigit