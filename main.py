import os
import datetime



print("\n >>>>>>>>>>>>> Menu <<<<<<<<<<<<<<<")
print(">> 1. Decrypt and View Entries <<")
print(">> 2. Encrypts and add Entries <<")
print(">> 3. Add in existing file <<")
print(">> 3. Remove a Entry <<")

choice = input("Enter a choice : ")

if choice == "1":
        print("Enter the file you want to view: ")
        filename = input("")    
        with open(filename, "r") as file:
             content = file.read()
             print(content)
        if os.path.exists(filename):
                os.system(f"gpg -d {filename}")
elif choice == "2":
        print("To proceed you would have to create a file to keep the entries stored : ")
        filename = input("")
  
        with open(filename,"a") as file: 
                current_date= datetime.datetime.now()
                date = str(current_date)
                task = input("Diary Entry : ")
                file.write(date + "\n")
                file.write(task + "\n")
                print("Entry added successfully")
        if os.path.exists(filename):
                os.system(f"gpg --symmetric {filename}")
        os.remove(filename)

elif choice == "3":
        filename = input("")
        if os.path.exists(filename):
                os.system(f"gpg -d {filename}")
        with open(filename,"a") as file: 
                current_date = datetime.datetime.now()
                date = str(current_date)
                task = input("Diary Entry : ")
                file.write(date + "\n")
                file.write(task + "\n")
                print("Entry added successfully")

elif choice == "4":
        print("Do you want to remove a file (note that the entry will be forever lost to the sands of time) : ")
        print("(y/n)")
        if "y" or "Y" or "Yes":
                filename = input("Enter the filename : ")
                os.remove(filename) 
        else:
               print("Nevermind.")     
else :
     print("Well, thank you for testing this humble program.")