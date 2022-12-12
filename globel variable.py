# # try 1

# l = 10  #Globle variable
# def function1(n):
#     l = 5 # local variable 1
#     m = 13 # local variable 2

#     print(l , m)
#     print(n,"I am a programer")

# function1("This is am amd")

l = 15 

def function2(n):
    global l #(this function allow for global variables and not allow for local varaibles)
    m = l+45

    print(m)

function()