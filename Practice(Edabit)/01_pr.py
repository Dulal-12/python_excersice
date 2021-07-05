def number_length(num):
    # s = 0
    # number = str(num)
    # for digit in number:
    #     s += 1
    # return s
    # print(s)
    return sum(1 for i in str(num))
number_length(123098765456789)
 
 