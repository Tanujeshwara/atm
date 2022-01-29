class Atm :
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    
    def check_balance(self):
        print("Your balance is Rs.50000")
    
    def withdrawal(self,amount):
        new_amount=50000-amount
        print("You have withdrawn amount  "+str(amount) +". Your remaining balance is "+str(new_amount))

def main():
    cardNumber=input("Insert your card number :")
    pinNumber=input("Enter your pin number :")
    new_user =Atm(cardNumber,pinNumber)
    print("choose your activity")
    print("1.Balance enquiry 2.Withdrawal")
    activity=int(input("enter your activity number :"))
    if(activity==1):
        new_user.check_balance()
    elif(activity==2):
        amount=int(input("enter the amount :"))
        new_user.withdrawal(amount)
    else:
        print("enter a valid number ")

main()




