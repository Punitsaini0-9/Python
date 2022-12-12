# Itrative Approch in Recursion

def factorial_Itrative(n):
    fac = 1
    for i in range(n):
        fac = fac * ( i +1 )

    return fac

    """
    :Punit n = Integer
    :return = n * n - 1 * n - 2 * n - 3 ...... 1
    """
    pass

# number = int(input("Enter the number here\n"))

# print(factorial_Itrative(number))


# Recursive approch in Recurtopn

def foctorial_recursive(n):

    """
    :Punit n = Integer
    :return = n * n + 1 * n + 2 * n + 3 ...... 1

    """

    if n == 1:
        return 1

    else:
        return n * foctorial_recursive(n -1)
        
        """
        How to work this function

        some example the no. is 5:
        5 * factorial_recusion(4)
        5 * 4 * factorial_recursion(3)
        5 * 4 * 3 * factorial_recusion(2)
        5 * 4 * 3 * 2 * factorial_recusion(1)
        5 * 4 * 3 * 2 * 1 = 120
        
        """

number = int(input("Enter the number here\n"))
print("Factorial using Rcorsive method", factorial_Itrative(number))
print("Factorial using Itrative method",foctorial_recursive(number))