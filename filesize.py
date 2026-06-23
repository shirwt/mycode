import os
from pathlib import Path 
a = Path(input("Enter the 1st file: "))
b = Path(input("Enter the 2nd file: "))

if a.exists() and b.exists():
    file_size = os.path.getsize(a)
    file2_size = os.path.getsize(b)
    print("File size of 1st file: ", file_size, "bytes")
    print("File size of 2nd file: ", file2_size, "bytes")
    if file_size >= file2_size:
        if file_size > file2_size:
            print("1st file is larger than 2nd file")
        else: 
            print("Size of both file is  equal")
    else:
        print("size of 2nd file is greater than 1st file")
else:
    print("THe file doesnt exists")


