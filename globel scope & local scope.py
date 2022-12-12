""""

# # try 1

# l = 10  #Globle variable
# def function1(n):
#     l = 5 # local variable 1
#     m = 13 # local variable 2

#     print(l , m)
#     print(n,"I am a programer")

# function1("This is am amd")

"""


"""

#  # try 2
l = 15 

def function2(n):
    # l = 5
    m = 6
    global l #(this function allow for global variables and not allow for local varaibles)
    l = l + 45
    print(l , m)
    print(n)
function2("hello")

"""

x = 89
def punit():
    x = 20

    def prashant():

        global x
        x = 88

    # print("before calling punit", x)

    prashant()

    print("after calling punit", x)

punit()
print(x)
