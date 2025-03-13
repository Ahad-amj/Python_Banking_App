![gif](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2c1OHRuZmxtbjFzZjF6NTVlZWc5OTRsNHF5YXh3YmUxOXpwdXpldSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BfFFYPSVYr9UR6EtEL/giphy.gif)

# The Project: Banking With Python 💳🏦

This project aims to develop a miniature banking system for ACME Bank, which uses a CSV file structure called `bank.csv` to manage customer accounts and transactions. The software will be used by cashiers to manage various operations, including logging in, adding new customers, performing deposits and withdrawals, and handling transactions between accounts.
<br><br>


### Technologies Used:🛠️

- **Python**: The code is written in Python, utilizing its versatile libraries and features.
- **VS Code**: Visual Studio Code is used as the primary Integrated Development Environment (IDE) to write and edit the Python code. All related files, including Python scripts, README.md, and CSV files, are stored and managed within the VS Code workspace.
- **GitHub**: GitHub is used for version control. Each time progress is made, the work is committed and pushed frequently to GitHub to ensure proper version tracking and collaboration.
<br><br>


## Functionality:⚙️

| Method | Description | 
|------------|-----------|
| Add New Customer |* customer can have a checking account<br>* customer can have a savings account<br>* customer can have both a checking and a savings account |
| Withdraw Money from Account (required login)|* withdraw from savings <br>* withdraw from checking |
| Deposit Money into Account (required login)|* can deposit into savings <br>* can deposit into checking|
| Transfer Money Between Accounts (required login)| * can transfer from savings to checking <br> * can transfer from checking to savings <br> * can transfer from checking or savings to another customer's account |
| Build Overdraft Protection | * charge customer ACME overdraft protection fee of $35 when overdraft <br> * prevent customer from withdrawing more than $100 USD if account is currently negative <br> * _the account cannot have a resulting balance of less than -$100_  <br> * _the customer cannot make a withdrawal of greater than $100_ <br> * deactivate the account after 2 overdrafts <br> * reactivate the account if the customer brings the account current, paying both the overdraft amount and the resulting overdraft fees |
<br><br>

### Challenges / Key Taskeaways from Experience:🚀

- Improved skills in efficiently searching for specific information.
- Gained proficiency in working with CSV files and directories in Python, as well as manipulating their data.
- Gained a better understanding of working with classes in Python.
- Learned to write code with a clear logic, ensuring all requirements are properly addressed.
 <br><br>

### Ice Box Feature:❄️

- Display Transaction Data (You need to create another file to store the transaction history, required login)
- index all transactions for a customer account
- show historical data of transactions (date and time of transaction, type of transaction, resulting balance, etc.)
- show one transaction **details**
- Unit Testing Based on **test-driven development (TDD)** approach

### References: 📚
I faced struggles trying to access the elements in the CSV file, so I did a lot of searching and found a YouTube [video](https://youtu.be/ZuxVxVj30ms?si=ZZyN2TMGCq2tazJ5) that explained a way to access the values in the file. It helped me a lot! 😄



