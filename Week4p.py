var = 100
if var < 200:
   print "Expression value is less than 200"
   if var == 150:
      print "Which is 150"
   elif var == 100:
      print "Which is 100"
   elif var == 50:
      print "Which is 50"
   elif var < 50:
      print "Expression value is less than 50"
else:
   print "Could not find true expression"

print "Good bye!"

'''b ={
    'a' : 122,
    'b' : 123,
    'c' : 124,
    'd' : 125
}

# take user input
inp = input('input a character : ')
# -1 is the default value if there is no keys that matches the input
val = b.get(inp, -1)
print('The result for inp is : ', val)'''