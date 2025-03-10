import csv
import os

def convert_acct_balance_info(info):
    if type(info) == "int":
        return float(info)
    else:
        return None

class Bank:
    
    banking_info = [
        { 'account_id': '10001',  'frst_name': 'suresh',  'last_name': 'sigera' , 'password':'juagw362',    'balance_checking':1000, 'balance_savings': 10000},
        { 'account_id': '10002', 'frst_name': 'james', 'last_name': 'taylor' , 'password':'idh36%@#FGd', 'balance_checking': 10000, 'balance_savings':10000}, 
        { 'account_id': '10003',  'frst_name': 'melvin', 'last_name': 'gordon' ,'password':'uYWE732g4ga1',    'balance_checking':2000, 'balance_savings':20000}, 
        { 'account_id': '10004', 'frst_name': 'stacey', 'last_name': 'abrams' ,'password':'DEU8_qw3y72$',    'balance_checking':2000, 'balance_savings':20000}, 
        { 'account_id': '10005',  'frst_name': 'jake', 'last_name': 'paul', 'password':'d^dg23g)@','balance_checking':100000,'balance_savings':100000}
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
            user_choice = int(input("How do you want it to be?\n1-acount for savings\n2-acount for checking\n3-acount for both\n"))

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
                        self.balance_checking = convert_acct_balance_info(col["balance_checking"])
                        self.balance_savings = convert_acct_balance_info(col["balance_savings"])
                        check_acct_num = False
                        break
                if check_acct_num:
                    print("Your account id is incorrect, Try again!!")
            check_password = True
            while check_password:
                user_password = input("Enter your password: ")
                if user_password == self.password:
                    print(f"Hello {self.first_name} {self.last_name} with the following acount id {self.account_id} !\nYour account checking balance is {str(self.balance_checking)}\nYour saving balance is {str(self.balance_savings)} .")
                    check_password=False
                else:
                    print("Your password is invalid! Try again!")

            try:

                user_operation = input("Do you want to do any operation? (Y/N): ").upper()
                if user_operation == "Y":
                    user_oper=int(input("Choose one of these:\n1- withdraw\n2- deposite\n3- transfer"))
                    if user_oper == 1:
                        operation=Operation(self)
                        operation.withdraw()
                    elif user_oper == 2:
                        operation=Operation(self)
                        operation.deposite()
                    # elif user_oper == 3:
                    #     operation=Operation(self)
                    #     operation.transfer()
                    else:
                        print("Invalid input choose between 1, 2 and 3")
            except ValueError:
                    print("Invalid input!! Please enter a valid number.")




            
            
     

    def log_out(self):
        user_log_out=input("Do you want to log out? (Y/N): ").upper()
        if user_log_out == "Y":
            print("You have been logged out!\nHave a nice day!")
        # elif user_log_out == "N":
            
        
        else:
            print("Invalid input! Please choose (Y/N).")




class Operation:
    def __init__(self, acount):
        self.account = account
        # with open("bank.csv", "r") as bank:
        #     data = csv.DictReader(bank)



    def withdraw(self):
        try:
            user_withdraw=int(input("Do you want to withdraw from savings or checking balance? 1- withdraw from saving balance\n2- withdraw from checking balance\n"))
            user_withdraw_amount=float(input("How much money do you want to withdraw? "))
    
            if user_withdraw == 1 and user_withdraw_amount <= 100 and self.account.balance_savings != None:
                self.account.balance_savings -= user_withdraw_amount
                # if self.balance_savings < 0:
                #     self.balance_savings -= user_withdraw_amount
            elif user_withdraw == 2 and user_withdraw_amount <= 100 and self.account.balance_checking != None:
                self.account.balance_checking -= user_withdraw_amount
                # if self.balance_checking < 0:
                #     self.balance_checking -= user_withdraw_amount
            else:
                print("You have this massage because one of the following reasons!\nnot choosing between 1 or 2\nthe user does not have either saving or checking acount\nyou can't withdraw more that 100.")
       
        except ValueError:
                    print("Invalid input!! Please enter a valid number.")
    

    def deposite(self):

        try:
            user_deposite=int(input("Do you want to deposite money to savings or checking balance? 1- deposite to saving balance\n2- deposite to checking balance\n"))
            user_deposite_amount=float(input("How much money do you want to deposite? "))

            if user_deposite == 1 and self.account.balance_savings != None:
                self.account.balance_savings += user_deposite_amount
            if user_deposite == 2 and self.account.balance_checking != None:
                self.account.balance_checking += user_deposite_amount
            else:
                print("Invalid number! Please enter 1 or 2")
        except ValueError:
                    print("Invalid input!! Please enter a valid number.")
    # def transfer(self):

  

            
        
        



        


# new_file = Bank()
# print(new_file)
# new=Customer()
# new.new_customer()
account = Account()  
account.log_in()
# account.log_out()
# oper=Operation()
# oper.withdraw()
