import csv
import os
import datetime


def convert_acct_balance_info(info):
    try:
        return float(info)  
    except ValueError:
        return None  

class Bank:
    
    banking_info = [
        { 'account_id': '10001',  'frst_name': 'suresh',  'last_name': 'sigera' , 'password':'juagw362',    'balance_checking':1000, 'balance_savings': 10000 , 'account_status':'active' , 'count_overdraft':0 },
        { 'account_id': '10002', 'frst_name': 'james', 'last_name': 'taylor' , 'password':'idh36%@#FGd', 'balance_checking': 10000, 'balance_savings':10000 , 'account_status':'active' , 'count_overdraft':0 }, 
        { 'account_id': '10003',  'frst_name': 'melvin', 'last_name': 'gordon' ,'password':'uYWE732g4ga1',    'balance_checking':2000, 'balance_savings':20000 , 'account_status':'active' , 'count_overdraft':0 }, 
        { 'account_id': '10004', 'frst_name': 'stacey', 'last_name': 'abrams' ,'password':'DEU8_qw3y72$',    'balance_checking':2000, 'balance_savings':20000 , 'account_status':'active' , 'count_overdraft':0 }, 
        { 'account_id': '10005',  'frst_name': 'jake', 'last_name': 'paul', 'password':'d^dg23g)@','balance_checking':100000,'balance_savings':100000, 'account_status':'active' , 'count_overdraft':0 }
    ]
        
    fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings","account_status","count_overdraft"]
        
        
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
        
        

class Customer:

    def __init__(self):
        bank_csv = open("bank.csv", "r")
        last_account = bank_csv.readlines()[-1]
        last_account = last_account.split(",")
        last_account_id = int(last_account[0])
        self.account_id = str(last_account_id + 1)
        self.fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings","account_status","count_overdraft"]

    def new_customer(self):
        try:
            user_response=int(input("Hello! Welcome to the Bank\nChoose 1 or 2:\n1- Log in\n2- Create an account\n"))
            if user_response == 1:
                user_acc=Account()
                user_acc.log_in()

            elif user_response == 2:

                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                password = input("Enter your password: ")
                user_choice = int(input("How do you want it to be?\n1-acount for savings\n2-acount for checking\n3-acoun  for both\n")) 

                balance_checking = None
                balance_savings = None  

                repeat=True
                while repeat:
                    try:
                        if user_choice == 1:
                           balance_savings = float(input("Enter you savings: "))
                           repeat=False  

                        elif user_choice == 2:
                            balance_checking = float(input("Enter you checking: "))
                            repeat=False 

                        elif user_choice == 3 :
                            balance_checking = float(input("Enter your checking: "))
                            balance_savings = float(input("Enter your savings: "))
                            repeat=False
                        else:
                            print("Invalid input!! choose between 1, and 3.")
                            return
                    except ValueError:
                        print("Invalid input!! Please enter a vali  number.") 

                    new_user = { 'account_id':self.account_id, 'frst_name': first_name,  'last_name': last_name ,'password':password, 'balance_checking':balance_checking,'balance_savings':balance_savings, 'account_status':'active','count_overdraft':0} 

                    try:
                        with open("bank.csv", "a+") as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                            writer.writerow(new_user)
                            print(f"New customer {first_name} {last_name} added successfully with account id = {self.account_id}!")
                    except csv.Error as e:
                        print(e)     
            else:
                print("Invalid input! Please choose 1 or 2")
        except ValueError:
                    print("Invalid input!! Please enter a valid number.")


    
class Account:

    def __init__(self):
        self.account_id = None
        self.first_name = None
        self.last_name = None
        self.password = None
        self.balance_checking = None
        self.balance_savings = None
        self.account_status = 'active'
        self.count_overdraft = 0
        self.transactions = []

    def log_transactions(self, transaction_type, transaction_amount):
        transaction_details = {
            'transaction_type': transaction_type,
            'transaction_amount': transaction_amount,
            'transaction_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction_details)

    @staticmethod  
    def show_transaction_detail(account):
        print(f"Transaction history for account id: {account.account_id}")
    
        if not account.transactions:
           print("No transactions found.")
           return
    
        last_transaction = account.transactions[-1]  
        print(f"Transaction type: {last_transaction['transaction_type']}")
        print(f"Transaction amount: {last_transaction['transaction_amount']}")
        print(f"Transaction date: {last_transaction['transaction_date']}")

     
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
                        self.account_status = col.get("account_status", "Active")
                        check_acct_num = False
                        break
                if check_acct_num:
                    print("Your account id is incorrect, Try again!!")

            check_password = True
            while check_password:
                user_password = input("Enter your password: ")

                if user_password == self.password:
                    print(f"Hello {self.first_name} {self.last_name} with the following acount id {self.account_id} !\nYour account checking balance is {self.balance_checking}\nYour saving balance is {self.balance_savings} .")
                    check_password=False
                else:
                    print("Your password is invalid! Try again!")
            
            try:
                oper_choice = True
                while oper_choice:

                    user_oper=int(input("Do you want to do any operation?\nChoose one of these:\n1- withdraw\n2- deposite\n3- transfer\n4- log out\n"))

                    if user_oper == 1:
                        operation=Operation(self)
                        operation.withdraw()

                    elif user_oper == 2:
                        operation=Operation(self)
                        operation.deposite()

                    elif user_oper == 3:
                        operation=Operation(self)
                        operation.transfer()

                    elif user_oper == 4:
                        print("You have been logged out!\nHave a nice day!")
                        oper_choice = False
                    
                    else:
                        print("Invalid input choose between 1, 2 and 3")
                
            except ValueError:
                    print("Invalid input!! Please enter a valid number.")

        

class Operation:

    def __init__(self, account):
        self.account = account
        self.fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings","account_status","count_overdraft"]
       
    def withdraw(self):
        try:
            if self.account.account_status == "deactivated":
                print("Your account has been deactivated due to overdrafts. Please deposit enough money to reactivate it.")
                return

            user_withdraw = int(input("Do you want to withdraw from savings or checking balance?\n1- withdraw from saving balance\n2- withdraw from checking balance\n"))

            if user_withdraw == 1 or user_withdraw == 2:
                user_withdraw_amount = float(input("How much money do you want to withdraw? "))

                if user_withdraw == 1 and self.account.balance_savings is not None:
                    if user_withdraw_amount <= 100:

                        if self.account.balance_savings - user_withdraw_amount < -100:
                            print("Withdrawal denied. Your savings account balance cannot go below -100.")
                            return

                        self.account.balance_savings -= user_withdraw_amount

                        if self.account.balance_savings < 0:
                            self.account.balance_savings -= 35
                            print(f"Your savings account balance went negative. A fee of 35 has been applied.")
                        print(f"Withdraw {user_withdraw_amount} from saving. Your new saving balance now is {self.account.balance_savings}.")
                        self.account.log_transactions("Withdrawal", user_withdraw_amount)
                        Account.show_transaction_detail(self.account)

                        if self.account.balance_savings < 0:
                            self.account.count_overdraft += 1
                            if self.account.count_overdraft > 2:
                                self.account.account_status = "deactivated"
                                print("Your account has been deactivated due to multiple overdrafts.") 

                    else:
                        print("You can't withdraw more than 100.")

                elif user_withdraw == 2 and self.account.balance_checking is not None:
                    if user_withdraw_amount <= 100:

                        if self.account.balance_checking - user_withdraw_amount < -100:
                            print("Withdrawal denied. Your checking account balance cannot go below -100.")
                            return

                        self.account.balance_checking -= user_withdraw_amount
                        
                        if self.account.balance_checking < 0:
                            self.account.balance_checking -= 35
                            print(f"Your checking account balance went negative. A fee of 35 has been applied.")

                        print(f"Withdraw {user_withdraw_amount} from checking. Your new checking balance now is {self.account.balance_checking}.")
                        self.account.log_transactions("Withdrawal", user_withdraw_amount)
                        Account.show_transaction_detail(self.account)

                        if self.account.balance_checking < 0:
                           self.account.count_overdraft += 1
                           if self.account.count_overdraft > 2:
                              self.account.account_status = "deactivated"
                              print("Your account has been deactivated due to multiple overdrafts.") 
                    else:
                        print("You can't withdraw more than 100.")
                else:
                    print("The user does not have an account.")

                self.update_new_balance()

            else:
                print("Invalid input, choose 1 or 2.")

        except ValueError:
            print("Invalid input!! Please enter a valid number.")


    def deposite(self):

        try:

            user_deposite=int(input("Do you want to deposite money to savings or checking balance?\n1- deposite to saving balance\n2- deposite to checking balance\n"))

            if user_deposite == 1 or user_deposite == 2:
                user_deposite_amount=float(input("How much money do you want to deposite? "))

                if user_deposite == 1 and self.account.balance_savings is not None:
                    self.account.balance_savings += user_deposite_amount
                    print(f"Deposite {user_deposite_amount} to saving. Your new saving balance now is {self.account.balance_savings} .")
                    self.account.log_transactions("Deposite", user_deposite_amount)
                    Account.show_transaction_detail(self.account)

                    if self.account.account_status == "deactivated" and self.account.balance_savings >0:
                        self.account.account_status = "active"
                        self.count_overdraft = 0
                        print("Your account has been reactivated!")

                elif user_deposite == 2 and self.account.balance_checking is not None:
                    self.account.balance_checking += user_deposite_amount
                    print(f"Deposite {user_deposite_amount} to checking. Your new checking balance now is {self.account.balance_checking} .")
                    self.account.log_transactions("Deposite", user_deposite_amount)
                    Account.show_transaction_detail(self.account)

                    if self.account.account_status == "deactivated" and self.account.balance_checking >0:
                        self.account.account_status = "active"
                        self.count_overdraft = 0
                        print("Your account has been reactivated!")
                    
                else:
                    print("Invalid account type!")

                self.update_new_balance()
            else:
                print("Invalid number! Please enter 1 or 2")
        except ValueError:
                    print("Invalid input!! Please enter a valid number.")

    
    def transfer(self):

        if self.account.account_status == "deactivated":
                print("Your account has been deactivated due to overdrafts. Please deposit enough money to reactivate it. ")
                return

        user_transfer = input("Enter the acount id you want to transfer to: ")
        
        if self.account.account_id == user_transfer:
            try:
                user_trans = int(input("Choose the account type that you want to transfer to\n1- saving\n2- checking\n"))
                trans_amount = float(input("How much money do you want to transfer? "))
                
                if self.account.balance_savings is not None and self.account.balance_checking is not None:
                    if user_trans == 1:
                        self.account.balance_savings += trans_amount
                        self.account.balance_checking -= trans_amount

                        print(f"you have successfully transfer {trans_amount} from checking account to saving account\nYour acount now has {self.account.balance_savings} in saving balance\n{self.account.balance_checking} in checking account.")
                        self.account.log_transactions("Transfer", trans_amount)
                        Account.show_transaction_detail(self.account)
                        
                    elif user_trans == 2:
                        self.account.balance_checking += trans_amount
                        self.account.balance_savings -= trans_amount

                        print(f"you have successfully transfer {trans_amount} from saving account to checking account\nYour acount now has {self.account.balance_savings} in saving balance\n{self.account.balance_checking} in checking account.")
                        self.account.log_transactions("Transfer", trans_amount)
                        Account.show_transaction_detail(self.account)

                    else:
                        print("Invalid input!! Please choose 1 or 2")
                    self.update_new_balance()
                else:
                    print("You just have one account\nYou can not transfer to yourself")

            except ValueError:
                    print("Invalid input!! Please enter a valid number.")

        else:
            account_found = False
            try:
                with open("bank.csv", "r") as bank:
                    data = csv.DictReader(bank)
                    for col in data:
                        if col["account_id"] == user_transfer:
                            self.first_name = col["frst_name"]
                            self.last_name = col["last_name"]
                            self.account_id = user_transfer
                            self.balance_checking = convert_acct_balance_info(col["balance_checking"])
                            account_found = True
                            break

                    if not account_found:
                        print("Account ID not found. Please check the account ID and try again.")
                        return

                    user_trans_others = int(input("Choose the account type that you want to do the transfer by\n1-  saving\n2- checking\n"))
                    amount_to_others = float(input("How much money do you want to transfer? "))

                    if user_trans_others == 1 or user_trans_others == 2:

                        if user_trans_others == 1 and self.account.balance_savings is not None:
                            self.balance_checking += amount_to_others
                            self.account.balance_savings -= amount_to_others

                            print(f"you have successfully transfer {amount_to_others} from your saving account to {self.  first_name} {self.last_name} account!\nYour acount now has {self.account.balance_savings} in  saving balance.")
                            print(f"{self.first_name} {self.last_name} account now has {self.balance_checking} in checking balance.")
                            self.account.log_transactions("Transfer", amount_to_others)
                            Account.show_transaction_detail(self.account)

                        elif user_trans_others == 2 and self.account.balance_checking is not None:
                            self.balance_checking += amount_to_others
                            self.account.balance_checking -= amount_to_others

                            print(f"you have successfully transfer {amount_to_others} from your checking account to {self.first_name} {self.last_name} account!\nYour acount now has {self.account.balance_checking} in checking balance.")
                            print(f"{self.first_name} {self.last_name} account now has {self.balance_checking} in checking balance.")
                            self.account.log_transactions("Transfer", amount_to_others)
                            Account.show_transaction_detail(self.account)

                        else:
                            print("Your account type is incorrect!")

                        self.update_new_balance()

                    else:
                        print("Invalid input!! Please choose 1 or 2")

            except ValueError:            
                print("Invalid input!! Please enter a valid number.")

    
                          

        
    def update_new_balance(self):
        updated = []
        with open("bank.csv", "r") as bank:
            data = csv.DictReader(bank)
            for col in data:
                if col["account_id"] == self.account.account_id:
                    col["balance_savings"] = str(self.account.balance_savings)
                    col["balance_checking"] = str(self.account.balance_checking)
                    col["account_status"] = self.account.account_status 
                    col["count_overdraft"] = self.account.count_overdraft 
                updated.append(col)

                if(hasattr(self, 'account_id')):
                    if col["account_id"] == self.account_id:
                        col["balance_checking"] = str(self.balance_checking)

        with open("./bank.csv", 'w', newline='') as csvfile:
            try:
                writer = csv.DictWriter(csvfile, fieldnames = self.fieldnames)
                writer.writeheader()
                for row in updated:
                    writer.writerow(row)
            except csv.Error as e:
                print(e)

    


customer=Customer()
customer.new_customer()
