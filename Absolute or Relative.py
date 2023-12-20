import os
file_path = input()
is_absolute = os.path.isabs(file_path)
print(is_absolute)