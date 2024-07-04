#logical operators (and,or,not)
temperature = int(input("what is the temperature today outside? "))
if temperature >=0 and temperature <30:   #and
    print("The temperature is good today")
    print("go outside !")
elif temperature >30 or temperature <0:   #or
    print("the temperature is bad today")
    print("I reccomend you not to go outside !")
#if not(temperature >30 or temperature <0):   #not
    #print("the temperature is bad today")
    #print("I reccomend you not to go outside !")
