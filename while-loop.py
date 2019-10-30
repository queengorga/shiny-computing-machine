password=''
while password != 'bea123':
    password=input("Enter password: ")
    if password == 'bea123':
        print("You are logged in!")
    else:
        print("Sorry, try again!")