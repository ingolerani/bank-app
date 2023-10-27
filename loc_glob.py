'''
x = 10 #global var

def fun1():
    global x
    y = 20 #local var
    y = y + 1
    x = x + 5
    print("locally in fun1, x=",x)#10
    print("locally in fun1, y=",y)#20
    #print("locally in fun1, z=",z)#NameError

def fun2():
    z = 30 #local var
    z = z * 2
    print("locally in fun2, x=",x)#10
    print("locally in fun2, z=",z)#30
    #print("locally in fun2, y=",y)#NameError

print("globally, x=", x)
#print("globally, y=", y)#NameError: name 'y' is not defined
#print("globally, z=", z) #NameError: name 'z' is not defined

fun1()
fun2()
'''

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






















































