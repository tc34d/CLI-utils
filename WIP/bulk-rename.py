import os
x=input("name of the folder/file(must be full path): ")
y=[]
z=0
if os.path.isdir(x): 
    print("\nIt is a directory")
    y.append(os.listdir(x))
    print(y)
    if input("input specific file or all files") == "all":
        src=y
    else:
        src=input("input specific file: ")
    
    dst=input("enter new name(there will be a number at the end of the name to deferentiate ): ")
    os.rename(src, dst)
elif os.path.isfile(x):  
    print("\nIt is a normal file")
    dst=input("enter new name")
    os.rename(x , x+dst)
else:  
    print("It is a special file (socket, FIFO, device file)" )
exit()

