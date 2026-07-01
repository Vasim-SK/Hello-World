#print * pattren in rows and columns 

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()


#print * in triangle pattren 

for i in range(5):
    for j in range(1, i+1):
        print("*", end = " ")
    print()


#print * in inverted triangle

for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or i == 1 or i+j == 6:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()