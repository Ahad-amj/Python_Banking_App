import csv
import os
class Bank:
    def __init__(self):

        # banking_info_dict = {}
    
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
        
        try:
            new_row = { 'account_id': '10006', 'frst_name': 'james', 'last_name': 'taylor' , 'password':'idh36%@#FGd','balance_checking':10000, 'balance_savings':10000}
            with open("bank.csv", "a+") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(new_row)
        except csv.Error as e:
            print(e)
    
    # def csv_to_dict(self):
    #     try: 
    #         with open("bank.csv", "r") as file:
    #             contents = csv.DictReader(file)
    #             reader = csv.reader(file)
    #             banking_info_dict = [row for row in contents]
    #             print(banking_info_dict)
    #             for row in contents:
    #                 # print(row) 
    #                 # for prop in fieldnames:
    #                 #     print(row[prop]) 
    #                 break
    #     except csv.Error as e:
    #         print(e)
        
    # def dict_to_csv(self):
    #     with open("bank.csv", "w", newline="") as f:
    #         w = csv.DictWriter(f, banking_info_dict.keys())
    #         w.writeheader()
    #         w.writerow(my_dict)


    
    # write method for deposit
        #def deposit
        #takes user, password, account, and change_amount parameter
        #have user log in
            #check to see if password paramater is the same as password in csv
            #change users account by the change_amount paramter
    
    # try:
    #     new_row = { 'account_id': '10006',  'frst_name': 'suresh',  'last_name': 'sigera' , 'password':'juagw362', 'balance_checking':1000, 'balance_savings':10000 }
    #     with open("bank.csv", "a+") as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #         writer.writerow(new_row)
    # except csv.Error as e:
    #     print(e)

    # def create_user(first_name, last_name):
    #     try


class Add:
   # def __init__(self):
        # self.fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings"]
        # self.account_id = account_id
        # self.first_name = first_name
        # self.last_name = last_name
        # self.password = password
        # self.balance_checking = balance_checking
        # self.balance_savings = balance_savings

        
    def new_customer(self):
        adding_user=input("Do you want to add new acount? (Y/N): ").upper()
        fieldnames = ["account_id", "frst_name", "last_name", "password", "balance_checking", "balance_savings"]
        if adding_user == "Y":
            account_id=10005
            balance_checking=0
            first_name=input("Enter your first name: ")
            last_name=input("Enter your last name: ")
            password=input("Enter your password: ")

            user_choice=int(input("How do you want it to be?\n1-acount for savings\n2-acount for checking\n3-scount for both"))
            if(user_choice == 1):
               account_id=account_id+1
               balance_savings=int(input("Enter your savings: "))
                new_user= { 'account_id':account_id,  'frst_name': first_name, 'last_name': last_name , 'password':password, 'balance_checking':None, 'balance_savings':balance_savings}
            if(user_choice == 2):
                account_id = account_id+1
                balance_checking=int(input("Enter your checking: "))
                new_user= { 'account_id':account_id,  'frst_name': first_name,  'last_name': last_name , 'password':password, 'balance_checking':balance_checking, 'balance_savings':None}
            if(user_choice == 3):
                account_id=account_id+1
                balance_checking=int(input("Enter your checking: "))
                balance_savings=int(input("Enter your savings: "))

               new_user= { 'account_id':account_id,  'frst_name': first_name,  'last_name': last_name , 'password':password, 'balance_checking':balance_checking, 'balance_savings':balance_savings}
            

            self.account_id=self.account_id+1
            new_user= { 'account_id': self.account_id,  'frst_name': self.first_name,  'last_name': self.last_name , 'password':self.password, 'balance_checking':self.balance_checking, 'balance_savings':self.balance_savings}
            try:
                with open("bank.csv", "a+") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames)
                    writer.writerow(new_user)
            except csv.Error as e:
                print(e)
        else:
            print("Have a nice day!")
   


    
# class User:
#     def __init__(self):
        
    
    
#     def user_name(self):
#         user_name=input("Hello, welcome to the Bank!\nEnter your name: ").title()
#         full_name= self.first_name+' '+self.last_name
#         if user_name == full_name:
#             user_password=input("Enter your password: ")
#             if user_password == self.password:
#                 input("Do you want to check your acount? (Y/N): ").upper()


        

new=Add()
new.new_customer()
# new_file = Bank()
# print(new_file)