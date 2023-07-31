import random
import re
print("WELCOME TO DHARM BANK")
class DharmBank:
    global acc_no
    def __init__(self):
        pass


    def create_account(self):

        global acc_no, balance, pay_deposit

        def if_invalid_name(name):
            splited_name = name.split()
            while ("1" in name) or ("2" in name) or ('2' in name) or ('3' in name) or ('4' in name) or (
                    '5' in name) or (
                    '6' in name) or ('7' in name) or ('8' in name) or ('9' in name) or ('0' in name) or (
                    ':' in name) or (
                    ';' in name) or ("'" in name) or ('#' in name) or ('(' in name) or (')' in name) or (
                    '[' in name) or (
                    ']' in name) or ('{' in name) or ('}' in name) or ('<' in name) or ('>' in name) or (
                    '=' in name) or (
                    '-' in name) or ('+' in name) or ('*' in name) or ('/' in name) or ('^' in name) or (
                    '%' in name) or (
                    '$' in name) or ('|' in name) or ('!' in name) or ('?' in name) or ('_' in name) or (
                    '.' in name) or (
                    '&' in name) or ('@' in name) or (len(splited_name) != 3):
                print("********** Invalid Name **********")
                name = str(input("Enter Name (name fathersname sirname) : "))
            return True
        def if_invalid_acc_type(acc_type):
            acc_type_list = ['saving', 'current']
            while acc_type not in acc_type_list:
                print("**********Invalid Account Type **********")
                acc_type = str(input("Enter Account Type (current or saving) : "))
                acc_type.lower()

        def if_invalid_mobile_number(mo_num):
            while len(mo_num) < 10:
                print("********** InValid Mobile Number **********")
                mo_num = (input("Enter Mobile Number : "))

        def if_invalid_pincode(pin_code):
            while len(str(pin_code)) != 6:
                print("********** InValid pin Code **********")
                pin_code = int(input("Enter Your Address Pin Code : "))

        def if_invalid_email(email_id):
            email_id = email_id.strip()
            splited_email = email_id.split()
            while ("@gmail.com" not in email_id) or "@gmail.com" == email_id or len(splited_email) > 1:
                print("********** InValid Email id **********")
                email_id = input("Enter Email Id : ")
                email_id.lower()

        def get_acc_no():
            acc_no = ""
            acc_list = []
            f = open("bank_details_.txt", "r")
            record_list = f.readlines()
            f.close()
            for record in record_list:
                attributes = record.split()
                acc_list.append(attributes[0])

            for i in range(0, 5):
                a = random.randint(1, 9)
                acc_no += str(a)
            while acc_no in acc_list:
                for i in range(0, 5):
                    a = random.randint(1, 9)
                    acc_no += str(a)
            return acc_no

        # account Type
        acc_type = str(input("Enter Account Type (current or saving) : "))
        acc_type = acc_type.strip()
        acc_type.lower()
        if_invalid_acc_type(acc_type)

        # Name
        name = str(input("Enter Name (yourname fathersname sirname) : "))
        if_invalid_name(name)
        name = name.capitalize()
        name = name.strip()
        name = re.sub(" +", " ", name)
        name = name.replace(" ", "_")

        # Pin Code
        pin_code = int(input("Enter Your Address Pin Code : "))
        if_invalid_pincode(pin_code)

        # Email Id
        email_id = input("Enter Email Id : ")
        email_id.lower()
        if_invalid_email(email_id)

        # Mobile Number
        mo_num = (input("Enter Mobile Number : "))
        if_invalid_mobile_number(mo_num)

        # Salary
        salary = int(input("Enter monthly income : "))
        if acc_type == "saving":
            print("You Must to Deposit 500 rupees")
            pay_deposit = input("Are you agree to pay 500 rupees deposit (yes or no) : ")
            pay_deposit.strip()
            pay_deposit.lower()
            # while (pay_deposit != "yes") or (pay_deposit != "no")
            if pay_deposit == "yes":
                print(
                    "\n*********************************\n* ACCOUNT CREATED SUCSECCFULLLY *\n*********************************\n")
                acc_no = get_acc_no()
                balance = 500
                print(f"Account Number : {acc_no}")

            elif pay_deposit == "no":
                print("Sorry You are not able to Create Account ")




        elif acc_type == 'current':
            if salary < 100000:
                print("You must have anual income at Least 1 Lakh rupees ")
            else:
                print("You Must to Deposit 10000 rupees")
                pay_deposit = input("Are you agree to pay 10000 rupees deposit (yes or no) : ")
                pay_deposit.lower()
                if pay_deposit == "yes":
                    print(
                        "*********************************\n* ACCOUNT CREATED SUCSECCFULLLY *\n*********************************")
                    acc_no = get_acc_no()
                    balance = 10000
                    print(f"Account Number : {acc_no}")


                elif pay_deposit == "no":
                    print("Sorry You are not able to Create Current Account ")

        if pay_deposit == "yes":
            f = open("bank_details_.txt", "a")
            f.write(f"{acc_no} {acc_type} {name} {mo_num} {pin_code} {email_id} {balance}\n")
            f.close()
    def show_detail(self,acc_no):
        self.acc_no = acc_no
        taken_acc_no = acc_no.strip()
        f = open("bank_details_.txt", "r")
        file = f.readlines()
        for i in file:
            splited_record = i.split()
            if splited_record[0] == acc_no:
                nam = splited_record[2]
                nam = nam.replace("_"," ")
                print(f"Name              : {nam}\nMobile Number     : {splited_record[3]}\nAddress(pin code) : {splited_record[4]}\nEmail id          : {splited_record[5]}\nAccount Type      : {splited_record[1]}\nAccount Number    : {splited_record[0]}\nBalance           : {splited_record[6]} rupees")
            f.close()

    def transaction(self,tr_type,acc_no,amount):
        self.acc_no = acc_no
        self.amount = amount
        self.tr_type = tr_type

        def change_amount(acc_no,amount):
            f = open("bank_details_.txt","r")
            record_list = f.readlines()
            f.close()
            for record in record_list:
                attributes = record.split()
                if attributes[0] == (acc_no):
                    current_index = record_list.index(record)
                    changed_record = record.split()
                    changed_record[6] = amount
                    record_list[current_index] = f"{changed_record[0]} {changed_record[1]} {changed_record[2]} {changed_record[3]} {changed_record[4]} {changed_record[5]} {changed_record[6]}\n"

            o = open("bank_details_.txt","w")
            o.write("")
            o.close()
            for record in record_list:
                f = open("bank_details_.txt","a")
                f.write(record)
                f.close()

        f = open("bank_details_.txt", "r")
        file = f.readlines()
        for i in file:
            splited_record = i.split()
            if splited_record[0] == str(acc_no):
                acc_type = splited_record[1]
                balance = int(splited_record[6])
                f.close()
                if acc_type == "saving":
                    if balance > amount :
                        limit = balance - amount
                    else:
                        limit = amount-balance
                    if self.tr_type == "d":
                        if (balance + amount) > 100000:
                            print(f"You can not diposit more than {limit} rupees")
                        else:
                            total = balance + amount
                            change_amount(acc_no, total)
                    elif self.tr_type == "w":
                        if balance < amount :
                            print(f"Your Balance : {balance}")
                            print("********** You can not withdrow **********")
                        else:
                            total = balance - amount
                            change_amount(acc_no,total)

                else:
                    if self.tr_type == "d":
                        total = amount + balance
                        change_amount(acc_no, total)
                    elif self.tr_type == "w":

                        if (balance - amount) < -100000 :
                            print(f"Your Balance : {balance}")
                            print("********** You can not withdrow **********")
                            print(f"You can not withdrow more than RS {balance+100000}")
                        else:
                            total = balance - amount
                            change_amount(acc_no,total)


    def if_invalid_account_number(self,acc_no):
        self.acc_no = acc_no
        f = open("bank_details_.txt", "r")
        record_list = f.readlines()
        f.close()
        for record in record_list:
            attributes = record.split()
            if attributes[0] == str(acc_no):
                return True
            else:
                print("Invalid Account Number ")
                return False
    def update_data(self,item,acc_no,new_data):
        self.item = item
        self.acc_no = acc_no
        self.new_data = new_data
        '''
        nm = name
        pn = mobile number
        pc = pin code
        id = email id
        '''
        index = 0
        if self.item == "nm":
            index = 2
        elif self.item == "pn":
            index = 3
        elif self.item == "pc":
            index = 4
        elif self.item == "id":
            index = 5

        f = open("bank_details_.txt", "r")
        record_list = f.readlines()
        f.close()
        for record in record_list:
            attributes = record.split()
            if attributes[0] == (acc_no):
                current_index = record_list.index(record)
                changed_record = record.split()
                changed_record[index] = new_data
                record_list[
                    current_index] = f"{changed_record[0]} {changed_record[1]} {changed_record[2]} {changed_record[3]} {changed_record[4]} {changed_record[5]} {changed_record[6]}\n"

        o = open("bank_details_.txt", "w")
        o.write("")
        o.close()
        for record in record_list:
            f = open("bank_details_.txt", "a")
            f.write(record)
            f.close()

    def show_all_details(self):
        print(f"|---------------|--------------|----------------------------------------|--------------|----------|-----------------------------------|-----------------|\n|ACCOUNT NUMBER | ACCOUNT TYPE |                  NAME                  | PHONE NUMBER | PIN CODE |             EMAIL ID              |     BALANCE     |\n|_______________|______________|________________________________________|______________|__________|___________________________________|_________________|")
        f = open("bank_details_.txt","r")
        file = f.readlines()
        for record in file:
            splited_record = record.split()
            if splited_record[1] == "saving":
                ac_type = splited_record[1]+" "
            else :
                ac_type = splited_record[1]
            nam = splited_record[2]
            #nam
            nam = nam.replace("_"," ")
            length = len(nam)
            space_required = 40 - length

            if length % 2 == 1:
                one_side = (space_required//2)+1
                second_side = space_required//2
            else:
                one_side = (space_required // 2)
                second_side = space_required // 2

            nam = (" "*one_side)+nam+(" "*second_side)
            #email id
            id = splited_record[5]
            id_length = len(id)
            space_required2 = 34 - id_length

            if id_length % 2 == 1:
                one_side2 = (space_required2 // 2)+1
                second_side2 = (space_required2 // 2)
            else:
                one_side2 = (space_required2 // 2)
                second_side2 = (space_required2 // 2)

            id = (" " * one_side2) + id + (" " * second_side2)

            balance = splited_record[6]
            b_length = len(balance)
            left_space = 17-b_length
            front = left_space // 2
            if left_space % 2 == 1 :
                end = (left_space // 2)+1
            else:

                end = (left_space // 2)
            balance = (" " * front)+balance+(" " * end)


            print(f"|     {splited_record[0]}     |    {ac_type}   |{nam}|  {splited_record[3]}  |  {splited_record[4]}  |{id} |{balance}|")
        print("|_______________|______________|________________________________________|______________|__________|___________________________________|_________________|")
    def delete_all_data(self):
        check = input("Are you sure want to delete all the data (yes/no) : ")
        while check != "yes" or check != "no":
            if check == "yes":
                f = open("bank_details_.txt", 'w')
                f.write("")
                f.close()
            elif check == "no":
                break
            else:
                check = input("Are you sure want to delete all the data (yes/no) : ")


o = DharmBank()

# o.show_all_details()

inp = "0"
while inp != "exit":
    if inp == '0':
        inp = input("1) Create account \n2) user panel\n3) Admin panel\n\nEnter option : ")
        inp.strip()
        if inp == '1':
            o.create_account()
            inp = '0'
        elif inp == '2':
            acc_no = input("Enter Your Account Number : ")
            acc_no.strip()
            f = open("bank_details_.txt", "r")
            record_list = f.readlines()
            f.close()
            for record in record_list:
                attributes = record.split()
                if attributes[0] == str(acc_no):
                    while inp == "2":
                        inp = input("3) show details \n4) trransaction \n\nEnter option : ")
                        inp.strip()
                        if inp == '3':
                            o.show_detail(acc_no)
                            inp = '2'
                        elif inp == '4':
                            while inp == "4" :
                                inp = input("5) deposit \n6) withdrow \n\nEnter option : ")
                                inp.strip()
                                if inp == '5':
                                    amount = int(input("Enter amount : "))
                                    o.transaction("d", acc_no, amount)
                                    print("Amount Credited\n")
                                    inp = '4'
                                elif inp == '6':
                                    amount = int(input("Enter amount : "))
                                    o.transaction("w", acc_no, amount)
                                    print("Amount Debited\n")
                                    inp = '4'
                                elif inp == "back":
                                    inp = "2"
                                elif inp == "exit":
                                    exit()
                                else:
                                    inp = "4"
                        elif inp == "back":
                            inp = '0'
                        elif inp == "exit":
                            exit()
                        else:
                            inp = "2"
        elif inp == '3':
            password = input("Enter Passsword : ")
            password.strip()
            if password == "12345":
                while inp == '3':
                    inp = input("7) update data \n8)show all details \n9) delete all data\n\nEnter : ")
                    inp.strip()
                    if inp == '7':
                        while inp == '7':
                            inp = input(
                                "11) update name\n12) update phone number \n13) update pin code \n14) update Email id \n\nEnter :  ")
                            inp.strip()
                            if inp == '11':
                                acc_no = input("Enter account number : ")
                                new = input("Enter new name : ")
                                new.strip()
                                new.strip()
                                new = re.sub(" +", " ", new)
                                new = new.replace(" ","_")
                                o.update_data("nm", acc_no, new)
                                print("SUCESSFULLY UPDATED\n")
                                inp = '7'
                            elif inp == '12':
                                acc_no = input("Enter account number : ")
                                new = input("Enter new phone number : ")
                                if len(new) == 10:
                                    o.update_data("pn", acc_no, new)
                                    print("SUCESSFULLY UPDATED\n")
                                    inp = '7'
                                else:
                                    print("Invalid phone number ")
                                    inp = "7"
                            elif inp == '13':
                                acc_no = input("Enter account number : ")
                                new = input("Enter new pin code : ")
                                if len(new) == 6:
                                    o.update_data("pc", acc_no, new)
                                    print("SUCESSFULLY UPDATED\n")
                                    inp = '7'
                                else:
                                    print("Invalid pin code ")
                                    inp = '7'
                            elif inp == '14':
                                acc_no = input("Enter account number : ")
                                new = input("Enter new Email id : ")
                                if ("@gmail.com" not in new) or "@gmail.com" == new  :
                                    print("Invalid Email id ")
                                    inp = '7'
                                else:
                                    o.update_data("id", acc_no, new)
                                    print("SUCESSFULLY UPDATED\n")
                                    inp = '7'
                            elif inp == 'back':
                                inp = '3'
                            elif inp == 'exit':
                                exit()
                            else:
                                inp = '7'
                    elif inp == '8':
                        o.show_all_details()
                        inp = "3"
                    elif inp == '9':
                        o.delete_all_data()
                        inp = "3"
                    elif inp == "back":
                        inp = '0'
                    elif inp == 'exit':
                        exit()
                    else:
                        inp = '3'

            else :
                print("Invalid Passsword")
                inp = '0'
        elif inp == "exit":
            exit()
        else:
            inp = '0'

print("\n\nWELCOME")

