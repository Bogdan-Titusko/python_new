# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(example_string1[:2] + example_string1[-2:])
print(example_string1.replace('llo b' , ''))


# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip('*'))


# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
print(example_string4.capitalize().replace('j','J'))
example_string4 = example_string4.capitalize()
example_string4 = example_string4.replace('j', 'J')
print(example_string4)



# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(var2.title() + ',' + var3.lower() + ' '+ var1.capitalize())


# Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode('utf-16'))

# Write a code to return True if cost is greater than 500$
example_string5 = "It cost me 1000.00$"
# example_string5 = input('How much it costs :')

# if example_string5 > str(500):
#     print(True)
# elif example_string5 < str(500):
#     print(False)
# else:
#     print('Try again')

if float(example_string5[-8:-1]) > 500:
    print(True)
else:
    print(False)