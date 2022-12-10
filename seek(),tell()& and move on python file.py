# # test 1
# x = open("Paisent.txt")

# print(x.tell())
# print(x.readline())
# print(x.tell())
# print(x.readline())
# print(x.tell())

# x.close()


x = open ("Paisent.txt")

x.seek(13)
print(x.readline())
x.close()