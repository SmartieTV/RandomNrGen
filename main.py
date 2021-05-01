import random
import os
import time
# This is my test python code, which checks for random numbers and their results.
# Coded by: Adrian (SmartieTV - smrtv.de)
# Firstly coded here: https://www.onlinegdb.com/zGtvKhY_Q
# Exaluation as a spreadsheet here: https://docs.google.com/spreadsheets/d/1ALLV_BxWJsyYjhKHVDhPOThEOOB1-158cf3iHoU_Dm0/edit?usp=sharing

#Define a spleeping time here (default = 0.1):
sleeptime = (0.1) #Please be aware, that this can cause lag, if set to a value below 0.1!


create = ("true")
a = 0 
b = 0
c = 0
d = 0 
e = 0
f = 0
g = 0 
h = 0
i = 0
j = 0

gen = 0


while create == ("true"):
    create = ("false")
    gen = gen + 1
    time.sleep(sleeptime)
    os.system("clear")
    randomnr = (random.randint(1,10))
    if randomnr == 1:
        a = a + 1
    elif randomnr == 2:
        b = b + 1
    elif randomnr == 3:
        c = c + 1
    elif randomnr == 4:
        d = d + 1
    elif randomnr == 5:
        e = e + 1
    elif randomnr == 6:
        f = f + 1
    elif randomnr == 7:
        g = g + 1
    elif randomnr == 8:
        h = h + 1
    elif randomnr == 9:
        i = i + 1
    elif randomnr == 10:
        j = j + 1
    
    numbers = {'1': a, '2': b, '3': c, '4': d, '5': e, '6': f, '7': g, '8': h, '9': i, '10': j}
    winner = max(numbers, key=numbers.get)
    print("")
    print("---------------")
    print("Gen " + str(gen))
    print("Most frequent: " + winner)
    print("")
    print("1: " + str(a))
    print("2: " + str(b))
    print("3: " + str(c))
    print("4: " + str(d))
    print("5: " + str(e))
    print("6: " + str(f))
    print("7: " + str(g))
    print("8: " + str(h))
    print("9: " + str(i))
    print("10: " + str(j))
    print("---------------")
    create = ("true")