import os

print("To proceed you would have to create a file to keep the entries stored : ")
filename = input("")
print("\n >>>>>>>>>>>>> Menu <<<<<<<<<<<<<<<")
print(">> 1. View Entries <<")
print(">> 2. Add Entries <<")
print(">> 3. Remove All Entries<<")
print(">> 4. Remove a specific line <<")

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
elif choice == "4":
     deletelines= int(input("Enter the line index you want to delete : "))
     with open(filename,"r") as file:
         lines = file.readlines()
     if 1 <= deletelines <= len(lines):
        with open(filename, "w") as file:
            for i, line in enumerate(lines, start=1):
                if i != deletelines:
                    file.write(line)
        print("Line removed successfully")
     else:
        print("Not a valid choice")
else :
     print("Well, thank you for testing this humble program.")