text="Hello\nyou are reading this\nHave a nice day"
with open ("test.txt", "w") as file: #"a"-appedn "w"-write "r"-read
    file.write(text)