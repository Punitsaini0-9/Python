# Design a calculator which will correctly solve all the problems except the following one:
# 45*3 = 555 , 56+9 = 77 , 56/6 = 4
# your program should takw oprators and the tow numbers as input for the user and then return the result.

while True:
    # Oprators
    print("Choise oprators")
    print("1 = Addition")
    print("2 = Substraction")
    print("3 = Multiply")
    print("4 = Divide")

    x = int(input("Choise an oprators(1-4):\n")) # choise oprators

    if x==1: # Addition
        a = int(input("Enter no. A\n"))
        b = int(input("Enter no. B\n"))

        if a == 56 and b == 9: # Faulty value code in addition
            print("sum = 77")

        else:
            c = a+b
            print("Sum = ",c)

    elif x == 2: # Substraction
        a = int(input("Enter no. A\n"))
        b = int(input("Enter no. B\n"))

        c = a-b

        print("Difference = ",c)

    elif x == 3: # Multiply
        a = int(input("Enter no. A\n"))
        b = int(input("Enter no. B\n"))

        if a == 43 and b == 3: # Faulty value code in multiply
            print("Product = 555")

        else:
            c = a*b
            print("Product = ",c)

    elif x == 4: # Divide
        a = int(input("Enter no. A\n"))
        b = int(input("Enter no. B\n"))

        if a == 56 and b == 6: # Faulty value code in divide 
            print("Quotient = 4")

        else:
            c = a/b
            print("Quotient = ",c)

    else:
        print("You entered wrong optators please try again") 