#nested loops

rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
enter=input("Enter the symbol which u wanna use ")
for i in range(rows):
    for j in range(columns):
        print(enter,end=" ")
    print()
