"""

Astonger star

given examples

first is:
*
**
***
****

and then

****
***
**
*

"""
while True:
    print("Pattern Printing")
    num = int(input("Enter the number hoe many rows you want\n"))
    print("Enter number 1 or 0")
    bool_val = int(input("1 for True value and 0 for False value"))

    if bool_val == 1:
        for i in range(0 , num + 1):
            print("*" , i)

    if bool_val == 0:
        for i in range(num , 0 , -1):
            print("*" , i)