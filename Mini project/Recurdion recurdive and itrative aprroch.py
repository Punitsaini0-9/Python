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

number = int(input("Enter the number here\n"))
print("Factorial using Rcorsive method", factorial_Itrative(number))
print("Factorial using Itrative method",foctorial_recursive(number))