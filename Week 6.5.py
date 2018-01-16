password = "changeme"
#enterpassword=input("Enter the password: ")

attempts=0

#while enterpassword !=password:
   #print("Invalid password, try again.")
    #enterpassword=input("Enter the password: ")
    #attempts +=1;

while input("Enter the password:") !=password and attempts <4:
    print("Invalid password, try again.")
    attempts +=1;
    
if attempts ==4:
    print("Access denied, please press enter to exit and contact security to reset your password")
    print("You tried",attempts+1,"times to enter correct password.")




     
