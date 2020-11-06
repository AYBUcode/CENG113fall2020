b ={
    'a' : 122,
    'b' : 123,
    'c' : 124,
    'd' : 125
}

# take user input
inp = input('input a character : ')
# -1 is the default value if there is no keys that matches the input
val = b.get(inp, -1)
print('The result for inp is : ', val)