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
                 for row in contents:
                     print(row) 
                     for prop in fieldnames:
                        print(row[prop]) 
        except csv.Error as e:
            print(e)
        
        # try:
        #     new_row = { 'account_id': '10006', 'frst_name': 'james', 'last_name': 'taylor' , 'password':'idh36%@#FGd','balance_checking':10000, 'balance_savings':10000}
        #     with open("bank.csv", "a+") as csvfile:
        #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #         writer.writerow(new_row)
        # except csv.Error as e:
        #     print(e)
    
    


    
   

# you should have balance savings and balance checkings as part of a their own classes, one class for checkings, one class for savings, they can have a reference, basically you can use the name of the customer as a way to identify where the accounts belong
#build the customer class here with it's init/constructor

    #customers have a name, accounts, username, password

    #USe the class method decorator
    #normally you could just call a new customer as customer = Customer(...args)
    #but because you want to use inputs, you can just use a static method/class method decorator

class Customer(Bank):
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

            if user_choice == 1:
               balance_savings=float(input("Enter your savings: "))
                
            elif user_choice == 2:
                balance_checking=float(input("Enter your checking: "))
                
            elif user_choice == 3 :
                balance_checking=float(input("Enter your checking: "))
                balance_savings=float(input("Enter your savings: "))
            else:
                print("Invalid input!!")
                return

            new_user = { 'account_id':self.account_id,  'frst_name': first_name,  'last_name': last_name , 'password':password, 'balance_checking':balance_checking, 'balance_savings':balance_savings}
           
            
            try:
                with open("bank.csv", "a+") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                    writer.writerow(new_user)
                    print(f"New customer {first_name} {last_name} added successfully!")
            except csv.Error as e:
                print(e)
        else:
            print("Have a nice day!")

   

    
class Log(Bank):
     def __init__(self):
        with open("bank.csv", "r") as bank:
            data = csv.DictReader(bank)
            for col in data:
                col[""]
            self.fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings"] 
     
    def log_in(self):
        user_first_name = input("Hello, welcome to the Bank!\nEnter first name: ").lower()
        user_last_name = input("Enter last name: ").lower()
        full_name= user_first_name+' '+user_last_name
        if  == full_name:
            user_password = input("Enter your password: ")
            if user_password == self.password:
                return f"Your account checking balance is {self.balance_checking}\nYour saving balance is {self.balance_savings} ."
    def log_out(self):

# class Operation:


        

new=Customer()
new.new_customer()
# new_file = Bank()
# print(new_file)