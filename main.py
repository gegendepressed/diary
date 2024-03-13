import os

print("To proceed you would have to create a file to keep the entries stored : ")
filename = input("")
print("\n >>>>>>>>>>>>> Menu <<<<<<<<<<<<<<<")
print(">> 1. View Entries <<")
print(">> 2. Add Entries <<")
print(">> 3. Remove All Entries<<")
print(">> 4. Encrypt Entries <<")
print(">> 5. Decrypt Entries <<")

choice = input("Enter a choice : ")

if choice == "1":
    if os.path.exists(filename):
        with open(filename, "r") as file:
             content = file.read()
             print(content)
    else:
         print(f"No such file: {filename}")
elif choice == "2":
    with open(filename,"a") as file:
        date = input("Diary Date :")
        task = input("Diary Entry : ")
        file.write(date + "\n")
        file.write(task + "\n")
        print("Entry added successfully")
elif choice =="3":
        os.remove(filename)
elif choice =="4":
        os.system(f"gpg --symmetric {filename}")
        print("File encrypted successfully.")
elif choice =="5":
        os.system(f"gpg -d {filename}")     
else :
     print("Well, thank you for testing this humble program.")