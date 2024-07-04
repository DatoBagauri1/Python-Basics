try:
    with open("textt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
