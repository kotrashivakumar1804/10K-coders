#---------------------------------------------sets-----------------------------------------------#
# #set
# s={1, 2, 3, 4, 5}
# print(s)
# print(type(s))
# print(len(s))
# #hashable elements
# print(hash(3))
# #update set
# s.add(6)
# print(s)
# s.update([7, 8, 9])
# print(s)
# #delete specific element
# s.remove(3)
# print(s)
# #delete entire set
# del s

#--------------------------------------------dictneary------------------------------------------------#

#Dictneary
# Dict1={1:"sachin",2:30,3:"pune"}
# print(Dict1)
# print(len(Dict1))

# Dict1[4]="cricket"
# print(Dict1)

# del Dict1[4]
# print(Dict1)

# del Dict1
# print(Dict1)

#-------------------------------------------------Account Privacy and Messaging-------------------------------------------------------#

# shiva=['likith','vanu','kiran','ram','anil','prabu','pranith']
# ram=['likith','shiva','priya','anil','sai','kiran']
# if set(shiva) & set(ram):  # Check if there are common friends
#     print("You can send messages to each other.")
# else:
#     account_type=input("Is your friend's account public or private: ")
#     if account_type == 'public' :
#         print('You can send message to each other')
#     else :
#         print('You cannot send message to each other')

#------------------------------------------------------------FizzBuzz-----------------------------------------------------------------#

# for i in range(1,21):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i}-fizzbuzz')
#     elif i%3==0:
#         print(f'{i}-fizz')
#     elif i % 5 == 0:
#         print(f'{i}-buzz')


#------------------------------------------------Armstrong number checking-------------------------------------------------------#

# v=int(input("Enter a number: "))
# count=len(str(v))
# d=v
# r=0
# while v > 0:
#     result=v % 10
#     r += result ** count 
#     v //=10
# if d==r:
#     print("It is a armstrong number")
# else:
#     print("It is not a armstrong number")


#--------------------------------------------------------Movie ticket booking system-------------------------------------------------------#

# def Movie_tickets(price,tickets):
#     total_amount=(price*tickets)
#     print(f'Total amount to be paid: {total_amount}')
#     if total_amount <= 1500:
#         print('Thank you for purchasing the tickets.')
#     elif total_amount > 1500 and total_amount <= 2000:
#         print('Complementary Gift Coke for you.')
#     elif total_amount > 2000:
#         print('Complementary Gift Popcorn And Coke for you.')
#     else:
#         print('Thank you visit again.')

# Movie_tickets(
#     int(input("Enter the price of ticket : ")),
#     int(input("Enter the number of tickets: "))
# )

#--------------------------------------------------------leap year checking-------------------------------------------------------#

# leap_year=int(input("Enter a year: "))

# if leap_year % 4 == 0 and (leap_year % 400 == 0 or leap_year % 100 != 0):
#     print(f'This is a leap year {leap_year}')
# else:
#     print(f'This is not a leap year {leap_year}')

#--------------------------------------------------------Elericity bill calculation-----------------------------------------------#

# check the elericity bill as per the units and prices
# units=float(input('Enter the number of units consumed: '))
# bill_amount=0
# if units <=100:
#     bill_amount=units*2
#     print(f'The bill amount of {units} consumed units is: {bill_amount} Rs')
# elif units <= 200:
#     on=units-100
#     bill_amount=100*2+on*3
#     print(f'The bill amount of {units} consumed units is: {bill_amount} Rs')
# elif units > 200:
#      one=units-200
#      co1=100*2+100*3
#      co3=one*5
#      bill_amount=co1+co3
#      print(f'The bill amount of {units} consumed units is: {bill_amount} Rs')
# else:
#     print(f'thank you for using our service')


#---------------------------------------------------------perfect number and perfect square-----------------------------------------------#

# def perfect_number(n):
#         i=1
#         sum=0
#         while i < n:
#             if n % i == 0:
#                 sum+=i
#             i+=1
#         if sum == n:
#             print('It is a perfect number')
#         else:
#             print('It is not a perfect number')

# def perfect_square(n):
#     c=1
#     is_perfect_square=False
#     while c < n:
#         if c*c == n:
#             is_perfect_square=True
#         c+=1
#     if is_perfect_square== True:
#         print(f"{n} is perfect square")
#     else:
#         print(f"{n} is not perfect square")

# x=input("Enter perfect number or perfect square: ")
# if x == "perfect_number":
#     perfect_number(int(input("Enter a number: ")))  
# elif x == "perfect_square":
#     perfect_square(int(input("Enter a number: ")))
# else:
#     print("Invalid input. Please enter 'perfect_number' or 'perfect_square'.")

#------------------------------------------------------------- Student Marks and Grade Calculation-----------------------------------------------#

# def get_marks(subjects, marks):
#     marks_dict={}
#     for i in range(len(subjects)):
#         marks_dict[subjects[i]]=marks[i]
#     return marks_dict

# def calculate_avg(marks_dict):
#     total_marks=0
#     for marks in marks_dict.values():
#         total_marks+=marks
#     Average=total_marks/len(marks_dict)
#     return Average

# def find_grade(Average):
#     if Average >= 90:
#         return 'A'
#     elif Average >= 75 :
#         return 'B'
#     elif Average >= 50 :
#         return 'C'
#     else:
#         return 'F'
    
# subjects=['Telugu','Hindi','English','Maths','Science']
# marks=list(map(int, input('Enter marks for each subject separated by space: ').split()))

# marks_dict=get_marks(subjects, marks)
# Average=calculate_avg(marks_dict)
# Grade=find_grade(Average)

# print('subject wise marks:',marks_dict)
# print('Average marks:',Average)
# print('Grade:',Grade)

#------------------------------------------------------- Shopping Cart System----------------------------------------------------------#

# n=input('Enter item name :').split(',')
# m = list(map(int, input('Enter item price:').split(',')))
# def add_items(n,m):
#     items={}
#     for i in n:
#         items[i]=m[n.index(i)]
#     print(items)
#     return items
    
# def calculated_bill(cart):
#     Total_bill=0
#     Expensive_item=''
#     cheaper_item=''     
#     for item, price in cart.items():
#         Total_bill+=int(price)
#         if price == max(cart.values()):
#             Expensive_item=f'{item} : {price}'
#         elif price == min(cart.values()):
#             cheaper_item=f'{item} : {price}'
#     print(f'Most expensive item: {Expensive_item}')
#     print(f'Cheapest item: {cheaper_item}')
#     print(f'Total bill before discount: {Total_bill}')
#     return Total_bill

# def Discount(Total_Bill):
#     if Total_Bill <= 10000:
#         d1=Total_Bill*0.05
#         print(f'you will get 5% Discount : {Total_Bill * 0.05}')
#         return Total_Bill-(Total_Bill * 0.05)
#     elif Total_Bill <= 20000:
#         d2=Total_Bill*0.1
#         print(f'you will get 10% Discount : {Total_Bill * 0.1}')
#         return Total_Bill-(Total_Bill * 0.1)
#     elif Total_Bill <= 29999:
#         d3=Total_Bill*0.2
#         print(f'you will get 20% Discount : {Total_Bill * 0.2}')
#         return Total_Bill-(Total_Bill * 0.2)
#     else:
#         print(f'you will get 30% Discount : {Total_Bill * 0.3}')
#         return Total_Bill-(Total_Bill * 0.3)
    
# Cart_Items=add_items(n,m)
# Total_Bill=calculated_bill(Cart_Items)
# Final_Bill=Discount(Total_Bill)
# print('--------------------------------------')
# print('Final Bill After Discount:',Final_Bill)
# print('--------------------------------------')

#----------------------------------------------- username and password validation only password strong & week checking-----------------------------------------------#

# user_name=input('enter the string :')
# password=input('enter the password :')
# def validate_password(password):
#     upper=False
#     lower=False
#     digit=False
#     special=False
#     for i in password:
#         if i.isupper():
#             upper=True
#         elif i.islower():
#             lower=True
#         elif i.isdigit():
#             digit=True
#         elif i in '!@#$%^&*':
#             special=True
#     missing=''
#     if len(password) >= 8:
#         print(f'username: {user_name}')
#         if not upper:
#             missing += 'uppercase letter '
#         if not lower:
#             missing += 'lowercase letter '
#         if not digit:
#             missing += 'numbers '
#         if not special:
#             missing += 'special character '
        
#     # correct =print(f'strong password: {password}') and print('Login successful') if len(missing) == 0 
#     # else print(f'weak password: {password}') and print(f'missing:{missing}')

#     if len(missing) == 0:
#         print(f'strong password: {password}')
#         print('Login successful')
#     else:
#         print(f'weak password: {password}')
#         print(f'{missing} is missing')

# validate_password(password)

#----------------------------------------------- username and password validation with space and length check-----------------------------------------------#

# user_name=input('enter the string :')
# password=input('enter the password :')
# def validate_username(user_name):
#     space=False
#     if len(user_name) >= 5:
#         pass
#     for i in user_name:
#         if i==' ' :
#             space=True
       
#     if space :
#         print(f'invalid username: {user_name} should not contain spaces')
#     else:
#         print(f'valid username: {user_name}')
# def validate_password(password):
#     upper=False
#     lower=False
#     digit=False
#     special=False
#     missing=''
#     for i in password:
#         if i.isupper():
#             upper=True
#         elif i.islower():
#             lower=True
#         elif i.isdigit():
#             digit=True
#         elif i in '!@#$%^&*':
#             special=True
#     if len(password) >= 8:
#         if not upper:
#             missing += 'uppercase letter '
#         if not lower:
#             missing += 'lowercase letter '
#         if not digit:
#             missing += 'numbers '
#         if not special:
#             missing += 'special character '
    
#     if missing == '':
#         print(f'strong password: {password}')
#     else:
#         print(f'weak password: {password}')
#         print(f'{missing} is missing')
# validate_username(user_name)
# validate_password(password)

#---------------------------------------Email and Password Validation if @ and . in gmail will be allowed---------------------------------------#

# Email=input('enter the email :')
# password=input('enter the password :')
# def valid_email(Email):
#     space,special,com=False,False,False
#     check=''
#     if '@' not in Email:
#         check+='@ is missing '
#     if '.' not in Email:
#         check+='. is missing '
#     if ' ' in Email:
#         check+='space is not allowed '
#     if len(check) == 0:
#         print(f'valid Email: {Email}')
#         return True
#     else:
#         print(f'invalid Email: {check}')  
#         return False
# def validate_password(password):
#     upper,lower,digit,special=False,False,False,False
#     missing=''
#     for i in password:
#         if i.isupper():
#             upper=True
#         if i.islower():
#             lower=True
#         if i.isdigit():
#             digit=True
#         if i in '!@#$%*':
#             special=True
#     if len(password) <= 12:
#         if not upper:
#             missing += 'uppercase letter'
#         if not lower:
#             missing += 'lowercase letter'
#         if not digit:
#             missing += 'numbers'
#         if not special:
#             missing += 'special character'
#     if len(missing) == 0:
#         print(f'strong password: {password}')
#         return True
#     else:
#         print(f'weak password: {password}')
#         print(f'{missing} is missing')
#         return False
# final_Email=valid_email(Email)
# final_Password=validate_password(password)
# if final_Email and final_Password:
#     print('Final Status: Login Successful 🎉')
# else:
#     print('Final Status: Login Failed ❌')

# ----------------------------------------------------  product management system  ------------------------------------------------------
# class Product:
#     def __init__(self,id,name,price,rating):
#         self.id=id
#         self.name=name
#         self.price=price
#         self.rating=rating
# class User:
#     def __init__(self):
#         self.products=[]
#     def add_product(self):
#         id=int(input('enter product id:'))
#         for product in self.products:
#             if product.id == id:
#                 print('product id already exists')
#                 print('-'*50)
#                 return
#         name=input('enter product name:')
#         if len(name) <= 7:
#             name += ' ' * (7-len(name))
#         price=float(input('enter product price:'))
#         rating=float(input('enter product rating:'))
#         product=Product(id,name,price,rating)
#         self.products.append(product)
#         print('product added successfully to the cart.....!')
#         print('-'*50)

#     def remove_product(self):
#         if(len(self.products) == 0):
#             print('cart is empty.....!')
#             return
#         id=int(input('enter product id to remove:'))
#         for product in self.products:
#             if product.id == id:
#                 self.products.remove(product)
#                 print('product removed successfully from the cart.....!')
#                 print('-'*50)
#                 return
#         print('product not found in the cart.....!')
#         print('-'*50)

#     def Update_product(self):
#         if(len(self.products) == 0):
#             print('cart is empty.....!')
#             return
#         id=int(input('Enter product id to update:'))
#         for product in self.products:
#             if product.id == id:
#                 while True:
#                     print('SELECT 1 -->update name')
#                     print('SELECT 2 -->update price')
#                     print('SELECT 3 -->update rating')
#                     print('SELECT 4 -->update all') 
#                     print('SELECT 5 -->save the changes and exit')
#                     print('-'*50)
#                     choice=int(input('Enter your choice:'))
#                     print('-'*50)
#                     match choice:
#                         case 1:
#                             name=input('Enter new product name:')
#                             product.name=name
#                             print('product name updated successfully.....!')
#                         case 2:
#                             price=float(input('Enter new product price:'))
#                             product.price=price
#                             print('product price updated successfully.....!')   
#                         case 3:   
#                             rating=float(input('Enter new product rating:'))
#                             product.rating=rating
#                             print('product rating updated successfully.....!')          
#                         case 4:
#                             name=input('Enter new product name:')
#                             price=float(input('Enter new product price:'))
#                             rating=float(input('Enter new product rating:'))
#                             product.name=name
#                             product.price=price
#                             product.rating=rating
#                             print('product details updated successfully.....!') 
#                         case 5:
#                             print('changes saved successfully.....!')
#                             return
#                         case _:
#                             print('invalid choice.....!')
#         print('product not found in the cart.....!')
#         print('-'*50)

#     def show_products(self):
#         if (len(self.products) == 0):
#             print('cart is empty.....!')
#             return
#         print('-'*40)
#         print(' | ID | Name   | Price | Rating |')
#         print('-'*40)
#         for product in self.products:
#             print(f' | {product.id} | {product.name} | {product.price} | {product.rating} |')
#         print('-'*40)

#     def search_product(self):
#         if (len(self.products) == 0):
#             print('cart is empty.....!')
#             return
#         print('-'*50)
#         print('1 ---> search with id')
#         print('2 ---> search with name')
#         print('-'*50)
#         choice=int(input('Enter your choice:'))
#         print('-'*50)
#         if choice == 1:
#             id=int(input('Enter product id to search:'))
#             for product in self.products:   
#                 if product.id == id:
#                     print('-'*40)
#                     print(' | ID | Name   | Price | Rating |')
#                     print('-'*40)
#                     print(f' | {product.id} | {product.name} | {product.price} | {product.rating} |')
#                     print('-'*40)
#                     print('-'*50)
#                     return
#             print('product not found in the cart.....!')
#             print('-'*50)
#         elif choice == 2:
#             name=input('Enter product name to search:')
#             for product in self.products:
#                 if len(name) <= 7:
#                     name += ' ' * (7-len(name))
#                 if product.name == name:
#                     print('-'*40)
#                     print(' | ID | Name   | Price | Rating |')
#                     print('-'*40)
#                     print(f' | {product.id} | {product.name} | {product.price} | {product.rating} |')
#                     print('-'*40)
#                     print('-'*50)
#                     return
#             print('product not found in the cart.....!')
#             print('-'*50)

#     def sort_price(self):
#         if (len(self.products) == 0):
#             print('No products in the cart.....!')
#             return
#         self.products.sort(key=lambda x: x.price, reverse=False)
#         print('products sorted by price in ascending order.....!')
#         print('-'*50)

#     def sort_rating(self):
#         if (len(self.products) == 0):
#             print('No products in the cart.....!')
#             return
#         self.products.sort(key=lambda x: x.rating, reverse=True)
#         print('products sorted by rating in descending order.....!')
#         print('-'*50)
        
# print('......$ Welcome to the Product Management System $......')
# print('-'*50)
# user=User()
# while True:
#     print('SELECT 1 -->Add product to the cart')
#     print('SELECT 2 -->Remove product from the cart')
#     print('SELECT 3 -->Update product details')
#     print('SELECT 4 -->Show all products in the cart')
#     print('SELECT 5 -->Search product in the cart')
#     print('SELECT 6 -->Sort products by price')
#     print('SELECT 7 -->Sort products by rating')
#     print('SELECT 8 -->save and Exit')
#     print('-'*50)
#     choice=int(input('Enter your choice:'))
#     print('-'*50)
#     match choice:
#         case 1: user.add_product()
#         case 2: user.remove_product()
#         case 3: user.Update_product()
#         case 4: user.show_products()
#         case 5: user.search_product()
#         case 6: user.sort_price()
#         case 7: user.sort_rating()
#         case 8:
#             print('Thank you for using the Product Management System. Goodbye!')
#             break
#         case _:
#             print('Invalid choice. Please try again.')
#             print('-'*50)

#-------------------------------------------PDBC (Python Database Connectivity)-------------------------------------------------------#

#import mysql driver
# import mysql.connector
# #bulding connection between database and python
# c =  mysql.connector.connect(
#     user='root',
#     password='K@18022004',
#     host='localhost',
#     database='pdbc',
# )
# #creating cursor
# crs=c.cursor()

# H='''
# create table student(
#     id int primary key,
#     name varchar(20),
#     age int);

# '''
# #executing the query
# crs.execute(H)

# #save the changes parmently in the database
# c.commit()

# #close the connection
# crs.close()
# c.close()
        

# import mysql.connector
# c =  mysql.connector.connect(
#     user='root',
#     password='K@18022004',
#     host='localhost',
#     database='pdbc',
# )

# crs=c.cursor()

# H='''
# insert into student values(1,'shiva',20),
# (2,'likith',21),
# (3,'kiran',22);

# '''

# crs.execute(H)

# c.commit()
# print('data inserted successfully')

# crs.close()
# c.close()

# import mysql.connector
# c =  mysql.connector.connect(
#     user='root',
#     password='K@18022004',
#     host='localhost',
#     database='pdbc',
# )

# crs=c.cursor()


# H='''
# insert into student values(%s,%s,%s);

# '''
# id=int(input('Enter id: '))
# name=input('Enter name: ')
# age=int(input('Enter age: '))

# crs.execute(H,(id,name,age))

# c.commit()
# print('data inserted successfully')

# crs.close()
# c.close()

# import mysql.connector
# c =  mysql.connector.connect(
#     user='root',
#     password='K@18022004',
#     host='localhost',
#     database='pdbc',
# )

# crs=c.cursor()


# H='''
# select * from student;

# '''
# crs.execute(H)
# b=crs.fetchall()
# for i in b:
#     print(i)

# c.commit()
# print('data inserted successfully')

# crs.close()
# c.close()

#-------------------------------------mini project on PDBC (Python Database Connectivity)-------------------------------------------------------#

import mysql.connector

con = mysql.connector.connect(
    user='root',
    password='K@18022004',
    host='localhost',
    database='pdbc'
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS bank(
    name VARCHAR(50),
    acc_no Bigint PRIMARY KEY,
    balance FLOAT
)
""")
con.commit()


class Bank:

    def create_account(self):
        name = input('Enter your name: ')
        acc_no = int(input('Enter your account number: '))
        balance = float(input('Enter initial deposit amount: '))

        q = 'INSERT INTO bank VALUES(%s,%s,%s)'

        try:
            cur.execute(q, (name, acc_no, balance))
            con.commit()
            print('Account created successfully.....!')
            print('-'*50)
        except mysql.connector.IntegrityError:
            print('Account number already exists.....!')
            print('-'*50)

    def deposit(self):
        acc_no = int(input('Enter your account number: '))
        amount = float(input('Enter amount to deposit: '))

        if amount <= 0:
            print('Invalid amount.....!')
            return

        q = 'UPDATE bank SET balance=balance+%s WHERE acc_no=%s'
        cur.execute(q, (amount, acc_no))

        if cur.rowcount > 0:
            con.commit()
            print('Amount deposited successfully.....!')
            print('-'*50)
        else:
            print('Account not found.....!')
            print('-'*50)

    def withdraw(self):
        acc_no = int(input('Enter your account number: '))
        amount = float(input('Enter amount to withdraw: '))

        if amount <= 0:
            print('Invalid amount.....!')
            return

        q = 'SELECT balance FROM bank WHERE acc_no=%s'
        cur.execute(q, (acc_no,))
        res = cur.fetchone()

        if res is not None:
            balance = res[0]

            if balance >= amount:
                q = 'UPDATE bank SET balance=balance-%s WHERE acc_no=%s'
                cur.execute(q, (amount, acc_no))
                con.commit()
                print('Amount withdrawn successfully.....!')
                print('-'*50)
            else:
                print('Insufficient balance.....!')
                print('-'*50)
        else:
            print('Account not found.....!')
            print('-'*50)

    def show_balance(self):
        acc_no = int(input('Enter your account number: '))
        q = 'SELECT * FROM bank WHERE acc_no=%s'
        cur.execute(q, (acc_no,))
        res = cur.fetchone()

        if res is not None:
            print(f'Name           : {res[0]}')
            print(f'Account Number : {res[1]}')
            print(f'Balance        : {res[2]}')
            print('-'*50)
        else:
            print('Account not found.....!')
            print('-'*50)

    def money_transfer(self):
        sender_acc_no = int(input('Enter sender account number: '))
        receiver_acc_no = int(input('Enter receiver account number: '))
        amount = float(input('Enter amount to transfer: '))

        if amount <= 0:
            print('Invalid amount.....!')
            return

        if sender_acc_no == receiver_acc_no:
            print('Sender and Receiver accounts cannot be the same.....!')
            return

        cur.execute(
            'SELECT * FROM bank WHERE acc_no=%s',
            (receiver_acc_no,)
        )

        if cur.fetchone() is None:
            print('Receiver account not found.....!')
            print('-'*50)
            return

        cur.execute(
            'SELECT balance FROM bank WHERE acc_no=%s',
            (sender_acc_no,)
        )

        res = cur.fetchone()

        try:
            if res is not None:
                balance = res[0]

                if balance >= amount:

                    cur.execute(
                        'UPDATE bank SET balance=balance-%s WHERE acc_no=%s',
                        (amount, sender_acc_no)
                    )

                    cur.execute(
                        'UPDATE bank SET balance=balance+%s WHERE acc_no=%s',
                        (amount, receiver_acc_no)
                    )

                    con.commit()
                    print('Amount transferred successfully.....!')
                    print('-'*50)
                else:
                    print('Insufficient balance.....!')
                    print('-'*50)
            else:
                print('Sender account not found.....!')
                print('-'*50)

        except Exception:
            con.rollback()
            print('Transaction rolled back.....!')
            print('-'*50)

    def close_account(self):
        acc_no = int(input('Enter your account number: '))

        q = 'DELETE FROM bank WHERE acc_no=%s'
        cur.execute(q, (acc_no,))
        con.commit()

        if cur.rowcount > 0:
            print('Account closed successfully.....!')
            print('-'*50)
        else:
            print('Account not found.....!')
            print('-'*50)

    def manager(self):
        q = 'SELECT * FROM bank'
        cur.execute(q)

        res = cur.fetchall()

        if len(res) == 0:
            print('No accounts found.....!')
            print('-'*50)
        else:
            for i in res:
                print(i)
            print('-'*50)
print('......$ Welcome to the Bank Management System $......')
print('-' * 50)
b = Bank()
while True:
    print('SELECT 1 --> Create Account')
    print('SELECT 2 --> Deposit')
    print('SELECT 3 --> Withdraw')
    print('SELECT 4 --> Show Balance')
    print('SELECT 5 --> Money Transfer')
    print('SELECT 6 --> Close Account')
    print('SELECT 7 --> Manager')
    print('SELECT 8 --> Exit')
    print('-' * 50)
    choice = int(input('Enter your choice: '))
    print('-' * 50)
    match choice:

        case 1: b.create_account()
        case 2: b.deposit()
        case 3: b.withdraw()
        case 4: b.show_balance()
        case 5: b.money_transfer()
        case 6: b.close_account()
        case 7: b.manager()
        case 8:
            print('Thank you for using the Bank Management System. Goodbye!')
            break

        case _:
            print('Invalid choice. Please try again.')