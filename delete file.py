import os
import shutil
path="empty"
try:
    shutil.rmtree(path) #delete a directory
    #os.rmdir(path) #delete a an empty directory
    #os.remove(path) #delete a file
except FileNotFoundError:
    print("Error while deleting file")
except PermissionError:
    print("Error you can't delete an empty file")
else:
    print("It was deleted successfully")

