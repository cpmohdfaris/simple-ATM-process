import mysql.connector as m


def get_connection():
    connection = m.connect(host="localhost", user="myusername", password="mypassword", database="mydatabase")
    return connection


def table():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("CREATE TABLE BANK(acc_no INT PRIMARY KEY,name VARCHAR(20),amt INT,pin INT)")
    con.commit()
    cursor.close()
    con.close()

# table() can call only at the first running otherwise it show tablename already exists

class Account:
    BankName = "STATE BANK OF INDIA"
    IFSC_code = "SBIN004154"
    balance = 1000


class Finds:

    @staticmethod
    def find_name(fna):  # method for finding the account name
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT name FROM BANK WHERE acc_no = (%s)", (fna,))
        result = cursor.fetchall()
        # print(result)
        cursor.close()
        con.close()
        for i in result:
            # print(i)
            return i[0]

    @staticmethod
    def find_balance(fnb):   # method for finding the account balance
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT amt FROM BANK WHERE acc_no = (%s)", (fnb,))
        result = cursor.fetchall()
        # print(result)
        cursor.close()
        con.close()
        for i in result:
            # print(i)
            return i[0]

    @staticmethod
    def find_acc(faa):  # method for finding the account number

        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT acc_no FROM BANK WHERE acc_no = (%s)", (faa,))
        result = cursor.fetchall()
        # print(result)
        cursor.close()
        con.close()
        for i in result:
            # print(i)
            return i[0]

    @staticmethod
    def find_pin(fpa):  # method for finding the pin of the account

        con = get_connection()
        cursor = con.cursor()
        cursor.execute("SELECT pin FROM BANK WHERE acc_no = (%s)", (fpa,))
        result = cursor.fetchall()
        # print(result)
        cursor.close()
        con.close()
        for i in result:
            # print(i)
            return i[0]


class Update: 
    # class for update Database details

    @staticmethod
    def update_name(una, unb): 
        # Function for update the name of Account Holder

        con = get_connection()
        cursor = con.cursor()
        cursor.execute("UPDATE BANK SET name=(%s) WHERE acc_no=(%s)", (una, unb))
        con.commit()
        con.close()
        cursor.close()

    @staticmethod
    def update_amt_wit(uwa, uwb): 
        # Function for update the amount of Account Holder after withdrawn

        con = get_connection()
        cursor = con.cursor()
        cursor.execute("UPDATE BANK SET amt= amt-(%s) WHERE acc_no=(%s)", (uwa, uwb))
        con.commit()
        con.close()
        cursor.close()

    @staticmethod
    def update_amt_dep(uda, udb): 
        # Function for update the amount of Account Holder after deposit

        con = get_connection()
        cursor = con.cursor()
        cursor.execute("UPDATE BANK SET amt= amt+(%s) WHERE acc_no=(%s)", (uda, udb))
        con.commit()
        con.close()
        cursor.close()

    @staticmethod
    def delete(da): 
        # Function for delete account

        con = get_connection()
        cursor = con.cursor()
        cursor.execute("DELETE FROM BANK where acc_no=(%s)", (da,))
        con.commit()
        con.close()
        cursor.close()


class New(Account): 
    # class for new bank account entries

    @staticmethod
    def insert(acc_no, name, amt, code): 
        # Function for insert new Account into Database
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("INSERT INTO BANK VALUES(%s,%s,%s,%s)", (acc_no, name, amt, code))
        con.commit()
        cursor.close()
        con.close()

    def ins(self, ia, ib, ic, ip):

        self.insert(ia, ib, ic, ip)


class NotEnoughBalance(Exception):
    # class for Exception Handling
    pass


class NoExistingAccount(Exception):
    # class for Exception Handling
    pass


class Exists(Account, Finds, Update): 
    # Class for Existing Accounts

    def deposit_exist(self, abc): 
        # Function for print Details after deposit amount

        self.update_amt_dep(abc, acc)
        print("-----------------------")
        print("ACCOUNT NUMBER IS ", acc)
        print(self.BankName, ",", self.IFSC_code)
        print("ACCOUNT HOLDER IS ", self.find_name(acc))
        print("BANK BALANCE IS ", self.find_balance(acc))
        print("-----------------------")

    def withdrawn_exist(self, abc): 
        # Function for print Details after Withdrawal amount

        self.update_amt_wit(abc, acc)
        print("-----------------------")
        print("ACCOUNT NUMBER IS ", acc)
        print(self.BankName, ",", self.IFSC_code)
        print("ACCOUNT HOLDER IS ", self.find_name(acc))
        print("BANK BALANCE IS ", self.find_balance(acc))
        print("-----------------------")

    def balance_check(self, bc): 
        # Function for check the balance

        print("-----------------------")
        print("ACCOUNT NUMBER IS ", bc)
        print(self.BankName, ",", self.IFSC_code)
        print("ACCOUNT HOLDER IS ", self.find_name(bc))
        print("BANK BALANCE IS ", self.find_balance(bc))
        print("-----------------------")


while True:

    n = input("DO YOU WANT TO CONTINUE \t PRESS Y or N =")

    if n == "y" or n == "Y":

        user = int(input("1.EXISTING USER \t 2.NEW USER \nEnter Your Choice :"))

        if user == 1: 
            # For existing user

            print("LOGIN IN ")
            acc = int(input("Enter Your Account Number :"))
            pin = int(input("Enter Your 4 digit PIN :"))

            y = Finds()
            z = y.find_acc(acc)
            k = y.find_pin(acc)

            try:
                if z == acc and k == pin:

                    choice = int(input("1.DEPOSIT \t2.WITHDRAWN \t3.BALANCE ENQUIRY\t4.DELETE ACCOUNT\t5.EXIT"))

                    if choice == 1: 
                        # for Deposit 

                        dep_amt = int(input("Enter Deposit Amount :"))
                        if dep_amt % 100 == 0:

                            customer = Exists()
                            customer.deposit_exist(dep_amt)

                        else:
                            print("---Please deposit valid cash, multiple of  100---")

                    elif choice == 2:
                        # for Withdrawal 

                        wit_amt = int(input("Enter the withdrawn amount :"))
                        p = Finds()
                        x = p.find_balance(acc) - wit_amt

                        if x > 1000:

                            if wit_amt % 100 == 0:

                                customer = Exists()
                                customer.withdrawn_exist(wit_amt)

                            else:
                                print("---Please withdraw multiple of 100---")
                        else:
                            print("--------Insufficient Balance----------")

                    elif choice == 3:
                        # for Balance check
                         
                        customer = Exists()
                        customer.balance_check(acc)

                    elif choice == 4:
                        # for delete account

                        p = Update()
                        p.delete(acc)
                        print("--YOUR ACCOUNT HAS BEEN DELETED SUCCESSFULLY--")

                    elif choice == 5:
        
                        break

                    else:
                        break
                else:
                    raise NoExistingAccount()

            except NoExistingAccount:

                print("---You are entered wrong ACCOUNT NUMBER or PIN---")

        elif user == 2:
            # For new users

            a = input("Enter Account Holder Name :")
            b = (input("Enter Your 8 Digit Account Number :"))
            if len(b) == 8:
                c = int(input("Enter Your 4 digit PIN :"))
                customer = New()
                bal = Account()
                customer.ins(b, a, bal.balance, c)
                print("YOU CAN CONTINUE YOUR PROCESS AS EXISTING USER ...")
            else:
                print("PLEASE ENTER 8 DIGIT ACCOUNT NUMBER..")

        else:
            print("You are entered wrong input please try again later...")

    else:
        break
