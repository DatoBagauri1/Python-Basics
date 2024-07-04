#dictionary
capitals={"USA":"Washington DC",
                  "Georgia":"Tbilisi",
                  "Japan":"Tokyo"}
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("Georgia")  #delete;(
print(capitals["USA"])
print(capitals.values())
print(capitals.keys())
print(capitals.items())
for key,value in capitals.items():
    print(key,value)