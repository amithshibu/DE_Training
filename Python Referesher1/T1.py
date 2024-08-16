#create login access using loop  and condition statement
while True:
    choice=input("enter option")
    if choice=='LOGIN':
        user=input("enter username")
        password=input("ente rpassword")
        if user=="admin" and password=="password":
            print("lohin successful")
        else:
            print("invalid credentials")
            
    elif choice=='quit':
        print("exiting from program")
        break
    else:
        print("invalid choice")
        