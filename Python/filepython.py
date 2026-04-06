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


# ---------------------------------------------------------Banking System-----------------------------------------------------------------#

balance=1000
def Deposit():
    amount=int(input('Enter the amount to be deposit:'))
    if amount > 0:
        print(f'{amount}/- Amount deposited successfully')
        return amount
    else:
        print('Invalid amount')
        return 0
def Withdraw():
    amount=int(input('Enter the amount to be withdraw:'))
    if amount <= balance:
        print(f'{amount}/- Amount withdraw successfully')
        return amount
    else:
        print('Insufficient balance')
        return 0
def CheckBalance():
    print(f'Your current balance is {balance}/-')

print('<------$---Welcome to the Bank of India---$------>')
ACC_Pin=2004
Pin=int(input('Enter your pin: '))
chances=3
is_acc_pin_correct=False

for i in range(1,chances+1):
    if Pin == ACC_Pin:
        is_acc_pin_correct=True
        print('Welcome to our bank. Please select your transaction.')
        break
    else:
        if chances-i !=0:
            print(f'Incorrect pin. You have {chances-i} chances left.')
            Pin=int(input('Enter your pin: '))
        else:
            break
if is_acc_pin_correct:
    while True:
        print('Deposit press -------> 1')
        print('Withdraw press ------> 2')
        print('Check Balance press -> 3')
        print('Exit press ----------> 4')
        chose=int(input('Enter your choice: '))
        if chose == 1:
            balance += Deposit()
        elif chose == 2:
            balance -= Withdraw()
        elif chose == 3:
            CheckBalance()
        elif chose == 4:
            print('Thank you for using our services. Have a nice day!')
            break
        else:
            print('Invalid choice. Please try again.......!')
else:
    print('Your account is Temporarily blocked. Try after 24 hours or try again later.......!')