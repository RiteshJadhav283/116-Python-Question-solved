source_file=input("Enter the source file name: ")
destination_file=input("Enter the destination file name: ")

with open(source_file,'r') as src, open(destination_file,'w') as dest:
    dest.write(src.read())