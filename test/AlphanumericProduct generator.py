import sys

fsock = open('out.log', 'w')
myLetters = 'C','D','F','G','H','J','K','P','R','S','T','V','X','Y','Z'

for letter1 in (myLetters):
   for num in range(1000,9999):
       my_string = str(num) + letter1 + '\n'
       fsock.write(my_string)
#        print(my_string)

for letter1 in (myLetters):
   for letter2 in (myLetters):
       for num in range(100,999):
           my_string = str(num) + letter1 + letter2 + '\n'
           fsock.write(my_string)
#            print(my_string)

for letter1 in (myLetters):
   for letter2 in (myLetters):
       for letter3 in (myLetters):
           for num in range(10,99):
               my_string = str(num) + letter1 + letter2 + letter3 + '\n'
               fsock.write(my_string)
#                print(my_string)

for letter1 in (myLetters):
   for letter2 in (myLetters):
       for letter3 in (myLetters):
           for letter4 in (myLetters):
               for num in range(1,9):
                   my_string = str(num) + letter1 + letter2 + letter3 + letter4 + '\n'
                   fsock.write(my_string)
#                    print(my_string)

for letter1 in (myLetters):
   for letter2 in (myLetters):
       for letter3 in (myLetters):
           for letter4 in (myLetters):
               for letter5 in (myLetters):
                   my_string = letter1 + letter2 + letter3 + letter4 + letter5 + '\n'
                   fsock.write(my_string)
#                    print(my_string)

fsock.close()
