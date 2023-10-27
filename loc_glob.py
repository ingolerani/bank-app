balance = 0
def check_balance():
    print("Total Balance:", balance)

def deposit(amt):
    global balance
    balance = balance + amt
    print(amt,"Rs. deposited!")

def withdraw(amt):
    global balance
    '''
    if amt <= balance:
        balance = balance - amt
        print(amt,"Rs. withdrawn!")
    else:
        print("Insufficient Funds")
        check_balance()
    '''
    if amt >= balance:
        print("Insufficient Funds")
        check_balance()
    else:
        balance = balance - amt
        print(amt,"Rs. withdrawn!")
        

while True:
    ch = int(input("\n\n1.Deposit\t2.Withdraw\n3.Check Balance\t4.Exit"))
    if ch == 1:
        print("code for deposit")
        d_amt = int(input("Enter Amt To Deposit:"))
        deposit(d_amt)
    elif ch == 2:
        print("code for Withdraw")
        w_amt = int(input("Enter Amt To Withdraw:"))
        withdraw(w_amt)      
    elif ch == 3:
        print("code for Check Balance")
        check_balance()
    elif ch == 4:
        print("code for Exit")
        break
    else:
        print("Invalid Choice")






















































