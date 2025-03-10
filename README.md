
# The Project: Banking With Python

This project aims to develop a miniature banking system for ACME Bank, which uses a CSV file structure called `bank.csv` to manage customer accounts and transactions. The software will be used by cashiers to manage various operations, including logging in, adding new customers, performing deposits and withdrawals, and handling transactions between accounts.




### Functionality:
   - Add New Customer
       * customer can have a checking account
       * customer can have a savings account
       * customer can have both a checking and a savings account
   - Withdraw Money from Account (required login)
       * withdraw from savings
       * withdraw from checking
   - Deposit Money into Account (required login)
       * can deposit into savings
       * can deposit into checking
   - Transfer Money Between Accounts (required login)
       * can transfer from savings to checking
       * can transfer from checking to savings
       * can transfer from checking or savings to another customer's account
   - Build Overdraft Protection
       * charge customer ACME overdraft protection fee of $35 when overdraft
       * prevent customer from withdrawing more than $100 USD if account is currently negative
           * _the account cannot have a resulting balance of less than -$100_
             OR
           * _the customer cannot make a withdrawal of greater than $100_
       * deactivate the account after 2 overdrafts
           * reactivate the account if the customer brings the account current, paying both the overdraft amount and the
             resulting overdraft fees
   - **BONUS**
     - Display Transaction Data (You need to create another file to store the transaction history, required login)
     - index all transactions for a customer account
     - show one transaction **details**
     - show historical data of transactions (date and time of transaction, type of transaction, resulting balance, etc.)
     - Unit Testing Based on **test-driven development (TDD)** approach



