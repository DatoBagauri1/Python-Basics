#1.slicing indexing[]    [start,stop,step] &  2.slice()
#1
car = "nissan silvia "
funky_car = car[0:13:3]
first_letter = car[0:6]
last_letter = car[7:13]
reversed_car = car[::-1] #reversed string
print(first_letter)
print(last_letter)
print(funky_car)
print(reversed_car)

print("  ")
#2
website1= "http://youtube.com"
website2="http://google.com"
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])

