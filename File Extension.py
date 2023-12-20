import os
filename = input()
file_extension = os.path.splitext(filename)[1][1:]
print(file_extension)