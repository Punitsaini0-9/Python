# x = open("Paisent.txt","x")

# def Punit():
#    lines = ['Paisent','I am a Punit saini']
   

#    with open("Paisent.txt","a") as f:
#       for line in lines:

#          line = str(input())

#          f.write(line)
#          # f.write('\n')

# Punit()

# print(Punit)
line = ['Punit','saini']
with open('Paisent.txt','w') as f:

   f.write('\n'.join(line))

more_line = ['','i am punit sainio']

with open('Paisent.txt','a') as f:

   f.write('\n'.join(more_line))