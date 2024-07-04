#index operator
name="dato Baga$"
#if(name[0].islower()):
    #name=name.capitalize()
#print(name)
firstName=name[0:4].upper()
lastName=name[5:].lower()
lastcharacter=name[-1]
print(firstName)
print(lastName)
print(lastcharacter)