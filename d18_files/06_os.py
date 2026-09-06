import os 


a = os.listdir("dir") # this command will give you the list of the files which was present in the dir folder 
print(a)
print(os.getcwd()) # it willl giv me the locatin where i am right now 
print(os.path.exists("harry")) # tell me true or false if the file is exit or not 
os.remove("sample.txt")  # it will remove the fle 
os.rmdir("dir") # this command will rmemove only the empty folder or directory 