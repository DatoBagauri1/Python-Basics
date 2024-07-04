#str.formats
animal="Monkey"
object="moon"
#print("the "+animal+" "+"jumped over the "+object+"!")
print("The {} jumped over the {} !".format(animal,object)) #str.format
print("The {0} jumped over the {1} !".format(animal,object)) #positional argument
#print("The {} jumped over the {} !".format(animal="cow",object="moon")) #str.format
name="Bro"
print("Hello my name is {:<10} nice to meet you".format(name))
print("Hello my name is {:>10} nice to meet you".format(name))
number1=3.14367
print("the pi is {:.2f}".format(number1))
number2=1000
print("the pi is {:b}".format(number2))
print("the pi is {:o}".format(number2))
print("the pi is {:X}".format(number2))
print("the pi is {:e}".format(number2))
