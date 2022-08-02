
print('Hi please enter your name ')
user_name = input("Name : ")
last_name = input("Last name : ")
age = input("Age : ")
print( 'Hello ' + last_name + ' ' + user_name + '.' + 'Your age is '  + age)



a = 3
b = 4
c = None


hypotenuse = c = math.sqrt(a * a + b * b)

print(int(hypotenuse))



a  = float(input('Enter first lenght '))  #6
b  = float(input('Enter second lenght ')) #8
c = float(input('Enter third lenght '))   #10

trianlge =(c*c == a * a + b * b )
print(trianlge)


user = input(['Enter list'])

print(user[::-1])


a = ('1', '2', '3', '5', '8')
b = ('8', '2', '5')

a = list(a)
a.insert(2, b[2])
a.insert(2, b[1])
a.insert(2, b[0])
a = tuple(a)


print(a)
