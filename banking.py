import csv
import os
class Bank:
    
        banking_info = [
            { 'account_id': '10001',  'frst_name': 'suresh',  'last_name': 'sigera' , 'password':'juagw362',     'balance_checking':1000, 'balance_savings':10000},
            { 'account_id': '10002', 'frst_name': 'james', 'last_name': 'taylor' , 'password':'idh36%@#FGd',     'balance_checking':10000, 'balance_savings':10000}, 
            { 'account_id': '10003',  'frst_name': 'melvin', 'last_name': 'gordon' ,'password':'uYWE732g4ga1',     'balance_checking':2000, 'balance_savings':20000}, 
            { 'account_id': '10004', 'frst_name': 'stacey', 'last_name': 'abrams' ,'password':'DEU8_qw3y72$',     'balance_checking':2000, 'balance_savings':20000}, 
            { 'account_id': '10005',  'frst_name': 'jake', 'last_name': 'paul', 'password':'d^dg23g)@', 'balance_checking':100000,     'balance_savings':100000}
        ]
        
        fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings"]
        
        
        if not os.path.exists("./bank.csv"):
            with open("./bank.csv", 'w', newline='') as csvfile:
                try:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in banking_info:
                        writer.writerow(row)
                except csv.Error as e:
                    print(e)
        try: 
            with open("bank.csv", "r") as file:
                 contents = csv.DictReader(file)
                #  for row in contents:
                #      print(row) 
                #      for prop in fieldnames:
                #         print(row[prop]) 
        except csv.Error as e:
            print(e)
        
        
    
    
   

# you should have balance savings and balance checkings as part of a their own classes, one class for checkings, one class for savings, they can have a reference, basically you can use the name of the customer as a way to identify where the accounts belong
#build the customer class here with it's init/constructor

    #customers have a name, accounts, username, password

    #USe the class method decorator
    #normally you could just call a new customer as customer = Customer(...args)
    #but because you want to use inputs, you can just use a static method/class method decorator

class Customer:
    def __init__(self):

        bank_csv = open("bank.csv", "r")
        last_account = bank_csv.readlines()[-1]
        last_account = last_account.split(",")
        last_account_id = int(last_account[0])
        self.account_id = str(last_account_id + 1)
        self.fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings"]

    def new_customer(self):
        adding_user = input("Do you want to add new acount? (Y/N): ").upper()
         
        if adding_user == "Y":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            password = input("Enter your password: ")
            
            user_choice = int(input("How do you want it to be?\n1-acount for savings\n2-acount for checking\n3-scount for both\n"))
            balance_checking = None
            balance_savings = None
            repeat=True
            while repeat:
                try:
                    if user_choice == 1:
                       balance_savings=float(input("Enter your savings: "))
                       repeat=False
                        
                    elif user_choice == 2:
                        balance_checking=float(input("Enter your checking: "))
                        repeat=False
                        
                    elif user_choice == 3 :
                        balance_checking=float(input("Enter your checking: "))
                        balance_savings=float(input("Enter your savings: "))
                        repeat=False
                    else:
                        print("Invalid input!! choose between 1, 2 and 3.")
                        return
                except ValueError:
                    print("Invalid input!! Please enter a valid number.")
    
            new_user = { 'account_id':self.account_id,  'frst_name': first_name,  'last_name': last_name , 'password':password, 'balance_checking':balance_checking, 'balance_savings':balance_savings} 
            
            try:
                with open("bank.csv", "a+") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                    writer.writerow(new_user)
                    print(f"New customer {first_name} {last_name} added successfully with account id = {self.account_id}!")
            except csv.Error as e:
                print(e)
        else:
            print("Have a nice day!")

   

    
class Account:

    def __init__(self):
        self.account_id = None
        self.first_name = None
        self.last_name = None
        self.password = None
        self.balance_checking = None
        self.balance_savings = None
        
     
    def log_in(self):
        with open("bank.csv", "r") as bank:
            data = csv.DictReader(bank)
            check_acct_num = True
            while check_acct_num:
                user_account_id = input("Hello, welcome to the Bank!\nEnter account id: ")
                for col in data:
                    if  col["account_id"] == user_account_id:
                        self.account_id = col["account_id"]
                        self.first_name = col["frst_name"]
                        self.last_name = col["last_name"]
                        self.password = col["password"]
                        self.balance_checking = col["balance_checking"]
                        self.balance_savings = col["balance_savings"]
                        check_acct_num = False
                        break
                    else:
                        print("Your account id is incorrect, Try again!!")
            check_password = True
            while check_password:
                user_password = input("Enter your password: ")
                if user_password == self.password:
                    print(f"Hello {self.first_name} {self.last_name} with the following acount id {self.account_id} !\nYour account checking balance is {self.balance_checking}\nYour saving balance is {self. balance_savings} .")
                    check_password=False
                else:
                    print("Your password is invalid! Try again!")
     

    def log_out(self):
        user_log_out=input("Do you want to log out? (Y/N): ").upper()
        if user_log_out == "Y":
            print("You have been logged out!\nHave a nice day!")
        # elif user_log_out == "N":
            
        
        else:
            print("Invalid input! Please choose (Y/N).")




class Operation(Account):
    def __init__(self):
    

    def withdraw(self):
        user_withdraw=input("Do you want to withdraw from savings or checking balance? 1- withdraw from saving balance\n2- withdraw from checking balance\n")
        user_withdraw_amount=float(input("How much money do you want to withdraw?"))

        # if user_withdraw == 1 and user_withdraw_amount<

  

            
        
        



        


# new_file = Bank()
# print(new_file)
# new=Customer()
# new.new_customer()
account = Account()  
# account.log_in()
account.log_out()
