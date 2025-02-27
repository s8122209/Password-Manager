#Password Manager
import os

try:
    #create a file to store credentials if it doesnt exist
    f = open("PasswordManager.txt", "x")
    f.close()
    f = open("PasswordManager.txt", "w")
    f.write("Login Credentials:\n")
    f.close()
except:
    pass

play = True

def addcreds():
    #Add new credentials
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    url = input("Enter your URL/Resource: ")
    f = open("PasswordManager.txt", "a")                                                                                           
    f.write(f"Email: {email} Password: {password} URL/Resource: {url}\n")
    f.close()
    print("Credentials saved.")
    
def viewcreds():
    #View credentials on file
    if os.path.getsize("PasswordManager.txt") == 0:
        print("No credentials saved.")
    else:
        f = open("PasswordManager.txt", "r")
        print(f.read())
        f.close()    

print("Welcome to the Password Manager!")

#Start the main loop
while play:
    print("1. Add new credentials")
    print("2. View credentials on file")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        #Add new credentials
        addcreds()
        continue
    elif choice == "2":
        #View credentials on file
        viewcreds()
        continue
    elif choice == "3":
        #Exit
        print("Goodbye!")
        break
    else:
        #invalid input
        print("Invalid choice. Please try again.")
        continue
