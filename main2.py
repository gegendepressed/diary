credentials = {'Sairaj' : '4209'}


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in credentials and credentials[username] == password :
        print("Welcome "+username)
        return True
    else:
        print("Who are you ?")
        return False
    
if login():
    print("To proceed you would have to create a file to keep the entries stored : ")
    name = input("")
    filename = name
    print("\n Menu")
    print("1. View Entries")
    print("2. Add Entries")

    choice = input("Enter a choice : ")
      
    if choice == "1":
        with open(filename, "r") as file:
            content = file.read()
            print(content)
            file.close()
    elif choice == "2":
        with open(filename,"a") as file:
            date = input("Diary Date : ")
            task = input("\n Diary Entry : ")
            file.write(date)
            file.write(task)
            file.close()
            print("Entry added successfully")
    
