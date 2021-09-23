import os

basepath = os.getcwd()

libname = input("Contract library name:")
path = os.path.join(basepath, libname)
if os.path.isdir(path):
	print("libname " + libname + " is already used")
	exit()
os.mkdir(path)

entryname = input("Contract entry name:")

print(libname)
print(entryname)

