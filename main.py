import os
import datetime
from pytermgui import tim
import signal
import sys
signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

tim.print("[bold !gradient(56)]Diary[/!]")

tim.print("[bold]1. Create New and Encrypt [/]")
tim.print("[bold]2. Decrypt and View [/]")
tim.print("[bold]3. Add to existing[/]")
tim.print("[bold red]4. Remove Entry[/]")
tim.print("Support me [skyblue underline ~https://github.com/gegendepressed]" + "on Github[/]!")

choice = input("Enter a choice : ")


if choice == "1":
        print("To proceed you would have to create a file to keep the entries stored : ")
        filename = input("")

        with open(filename,"a") as file: 
                current_date= datetime.datetime.now()
                date = str(current_date.strftime("Date : %D-%M-%Y Time : %H:%M:%S"))
                task = input("Diary Entry : ")
                file.write(date + "\n")
                file.write(task + "\n")
                print("Entry added successfully")
        if os.path.exists(filename):
                os.system(f"gpg --symmetric {filename}")
        os.remove(filename)
elif choice == "2":
        print("Enter the file you want to view: ")
        filename = input("")
        if os.path.exists(filename): 
                os.system(f"gpg -d {filename}")

elif choice == "3":
        filename = input("Enter the file you want to add : ")
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
        tim.print("Do you want to [bold red]remove[/] a file (note that the entry will be forever lost to the sands of time) : ")
        tim.print("[bold lightblue](Y/N)[/fg italic]!")
        if "y" or "Y" or "Yes":
                filename = input("Enter the filename : ")
                os.remove(filename) 
        else:
               print("Nevermind.")     
else :
     print("Well, thank you for testing this humble program.")

