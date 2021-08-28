data={}
print("Banking With Kamal Soni".center(100,'*'))
while True:
    print('\n')
    print("Main Menu".center(100,'-'))
    mc=int(input("""
1.New Account
2.Existing Account
3.Exit
Enter Choice:"""))

    if mc == 1:
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        city=input("Enter city:")
        atype=input("Enter Account Type(S/C):")
        amt=int(input("Enter Ammount:"))
        while True:
            no = int(input("Enter Account Number:"))
            if no in data.keys():
                print("Account Number Already Exist!! PLEASE RETRY...\n")
            else:
                data[no]=[name,age,city,atype,amt]
                print("\n---Account Created Succesfully---")
                break
    elif mc == 2:
        while True:
            uid=int(input("\nEnter Account Number:"))
            if uid in data.keys():
                while True:
                    print("\n")
                    print("User Portal".center(100,'-'))
                    uc=int(input("""
1.Check Balance
2.Withdraw
3.Deposit
4.Back To Main Menu
Enter Choice"""))
                    if uc == 1:
                        print("\nYour available Balance",data[uid][4])
                    elif uc == 2:
                        wd=int(input("Enter Withdraw Amount:"))
                        if wd<data[uid][4]:
                            data[uid][4]=data[uid][4]-wd
                            print("\nAmount Withdrawn\nYour Available Balance is",data[uid][4])
                        else:
                            print("Available balance is insufficient\n Try Again With Lower Amount!!")
                    elif uc == 3:
                        da=int(input("\nEnter Deposit Amount:"))
                        data[uid][4]=data[uid][4]+da
                        print("\nAmount Deposited\nYour Current balance is:",data[uid][4])
                    elif uc == 4:
                        break
                    else:
                        print("Invalid Input!! Please Retry")
                break
            else:
                print("\nInvalid Account Number!! PLEASE RETRY")
    elif mc == 3:
        break
    else:
        print("Invalid Input!! Please Retry")
print("\n")        
print("THANK YOU For Using Banking With Kamal Soni!!".center(100))

                
            
    
