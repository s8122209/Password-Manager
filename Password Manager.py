#Password Manager

try:
    #create a file to store credentials if it doesnt exist
    f = open("PasswordManager.txt", "x")
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
    found = False
    f = open("PasswordManager.txt", "r")
    user = input("Enter your email: ")
    for line in f:
        if user in line:
            print (f"Credentials found for {user}:\n")
            print(line)
            found = True
    if found != True:
        print ("Credentials not found.")
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
