class BankAccount:

    def __init__(self,user_name,ac_no,ph_no,i_amount):
        self.user_name = user_name
        self.ac_no = ac_no
        self.ph_no = ph_no
        self.i_amount = i_amount

    def credit(self,amt):
        self.amt = amt
        c = self.i_amount = self.i_amount + self.amt
        return c 
    
    def debit(self,amt):
        self.amt = amt
        d = self.i_amount = self.i_amount - self.amt
        return d

    def display(self):
        print("Current Balance: ", self.i_amount)

def usr_choice():
    ac_no = int(input("Enter your account number: "))
    amt = float (input("Amount: "))
    return amt
    
print("STARTING BANK SOFTWARE.....")
ask_usr = int(input("How many account do you have: "))

account_obj_list = []
for n in range (0,ask_usr):
    print("enter account information for user no: " + str(n+1))
    user_name = input("User Name: ")
    ac_no = int(input("Account No.: "))
    ph_no = int(input("Phone no.: "))
    i_amount = float(input("Initial amount: "))
    obj = BankAccount(user_name,ac_no,ph_no,i_amount)
    account_obj_list.append(obj)
    
print("STARTING CLIENT EXPERIENCE.....")

choice = input("What do you want to do? : credit/debit/check_balance : ")
if (choice == "credit"):
    x = usr_choice()
    obj.credit(x)

elif(choice == "debit"):
   y = usr_choice()
   obj.debit(y)

elif(choice == "check_balance"):
   obj.display()

else:
    print("OOPS!! WRONG CHOICE")
       