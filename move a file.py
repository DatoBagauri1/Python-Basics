import os
import shutil

source="test222"
destination="C:\\Users\\vbaga\\OneDrive"
try:
    if os.path.exists(destination):
        print("there is a file already in this destination")
    else:
        os.path.replace(source,destination)
        print("the file has been moved")

except FileNotFoundError:
  print("File"+source+"not found")

