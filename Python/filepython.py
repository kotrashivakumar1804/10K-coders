# # name=input("enter your name : ")
# # city=input("enter your city : ")
# # institute=input("enter your institute name : ")
# # course=input("enter your course : ")

# # var=f" I am {name}, came to {city} and joined in {institute} for {course} course."

# # # print(var)


# # #set
# # s={1, 2, 3, 4, 5}
# # print(s)
# # print(type(s))
# # print(len(s))
# # #hashable elements
# # print(hash(3))
# # #update set
# # s.add(6)
# # print(s)
# # s.update([7, 8, 9])
# # print(s)
# # #delete specific element
# # s.remove(3)
# # print(s)
# # #delete entire set
# # del s


# #Dictneary
# # Dict1={1:"sachin",2:30,3:"pune"}
# # print(Dict1)
# # print(len(Dict1))

# # Dict1[4]="cricket"
# # print(Dict1)

# # del Dict1[4]
# # print(Dict1)

# # del Dict1


# # print(Dict1)


# # shiva=['likith','vanu','kiran','ram','anil','prabu','pranith']
# # ram=['likith','shiva','priya','anil','sai','kiran']
# # if set(shiva) & set(ram):  # Check if there are common friends
# #     print("You can send messages to each other.")
# # else:
# #     account_type=input("Is your friend's account public or private: ")
# #     if account_type == 'public' :
# #         print('You can send message to each other')
# #     else :
# #         print('You cannot send message to each other')


# # for i in range(1,21):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print(f'{i}-fizzbuzz')
# #     elif i%3==0:
# #         print(f'{i}-fizz')
# #     elif i % 5 == 0:
# #         print(f'{i}-buzz')




# # v=int(input("Enter a number: "))
# # count=len(str(v))
# # d=v
# # r=0
# # while v > 0:
# #     result=v % 10
# #     r += result ** count 
# #     v //=10
# # if d==r:
# #     print("It is a armstrong number")
# # else:
# #     print("It is not a armstrong number")



# # def Movie_tickets(price,tickets):
# #     total_amount=(price*tickets)
# #     print(f'Total amount to be paid: {total_amount}')
# #     if total_amount <= 1500:
# #         print('Thank you for purchasing the tickets.')
# #     elif total_amount > 1500 and total_amount <= 2000:
# #         print('Complementary Gift Coke for you.')
# #     elif total_amount > 2000:
# #         print('Complementary Gift Popcorn And Coke for you.')
# #     else:
# #         print('Thank you visit again.')

# # Movie_tickets(
# #     int(input("Enter the price of ticket : ")),
# #     int(input("Enter the number of tickets: "))
# # )



# # leap_year=int(input("Enter a year: "))

# # if leap_year % 4 == 0 and (leap_year % 400 == 0 or leap_year % 100 != 0):
# #     print(f'This is a leap year {leap_year}')
# # else:
# #     print(f'This is not a leap year {leap_year}')


# # check the elericity bill as per the units and prices
# # units=float(input('Enter the number of units consumed: '))
# # bill_amount=0
# # if units <=100:
# #     bill_amount=units*2
# #     print(f'The bill amount of {units} consumed units is: {bill_amount} Rs')
# # elif units <= 200:
# #     on=units-100
# #     bill_amount=100*2+on*3
# #     print(f'The bill amount of {units} consumed units is: {bill_amount} Rs')
# # elif units > 200:
# #      one=units-200
# #      co1=100*2+100*3
# #      co3=one*5
# #      bill_amount=co1+co3
# #      print(f'The bill amount of {units} consumed units is: {bill_amount} Rs')
# # else:
# #     print(f'thank you for using our service')



# from os import CLD_STOPPED


# ecommerce_data = [
#     {
#         "order_id": "O1001",
#         "customer_name": "Ravi Kumar",
#         "city": "Hyderabad",
#         "product": "Wireless Mouse",
#         "category": "Electronics",
#         "price": 799,
#         "quantity": 2,
#         "total_amount": 1598,
#         "payment_method": "UPI",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1002",
#         "customer_name": "Sneha Reddy",
#         "city": "Bangalore",
#         "product": "Bluetooth Headphones",
#         "category": "Electronics",
#         "price": 1999,
#         "quantity": 1,
#         "total_amount": 1999,
#         "payment_method": "Credit Card",
#         "order_status": "Shipped"
#     },
#     {
#         "order_id": "O1003",
#         "customer_name": "Arjun Singh",
#         "city": "Mumbai",
#         "product": "Running Shoes",
#         "category": "Fashion",
#         "price": 2499,
#         "quantity": 1,
#         "total_amount": 2499,
#         "payment_method": "Cash on Delivery",
#         "order_status": "Processing"
#     },
#     {
#         "order_id": "O1004",
#         "customer_name": "Priya Sharma",
#         "city": "Delhi",
#         "product": "Smart Watch",
#         "category": "Electronics",
#         "price": 3499,
#         "quantity": 1,
#         "total_amount": 3499,
#         "payment_method": "Debit Card",
#         "order_status": "Delivered"
#     },
#     {
#         "order_id": "O1005",
#         "customer_name": "Kiran Patel",
#         "city": "Chennai",
#         "product": "Laptop Backpack",
#         "category": "Accessories",
#         "price": 1299,
#         "quantity": 3,
#         "total_amount": 3897,
#         "payment_method": "UPI",
#         "order_status": "Shipped"
#     }
# ]



# # for x in ecommerce_data:
# # #     if x["customer_name"] == x['customer_name']:
# # #         print(x['customer_name'])
# #        if x['price'] > 1000:
# #               print(x['customer_name'], x['price'])


# #print custoer names who is using upi method
# #print customer names who is purchasing other than electronics category
# #print customer names who is purchasing more than 1 quantity

# # for x in ecommerce_data:
# #     if x["payment_method"]=='UPI':
# #         print(x['customer_name'],x["payment_method"])

# #     if x['category'] != "Electronics":
# #          print(x['customer_name'],x["category"])

# #     if x["quantity"]>1:
# #         print(x['customer_name'],x["quantity"])

    

# # def perfect_number(n):
# #         i=1
# #         sum=0
# #         while i < n:
# #             if n % i == 0:
# #                 sum+=i
# #             i+=1
# #         if sum == n:
# #             print('It is a perfect number')
# #         else:
# #             print('It is not a perfect number')

# # def perfect_square(n):
# #     c=1
# #     is_perfect_square=False
# #     while c < n:
# #         if c*c == n:
# #             is_perfect_square=True
# #         c+=1
# #     if is_perfect_square== True:
# #         print(f"{n} is perfect square")
# #     else:
# #         print(f"{n} is not perfect square")

# # x=input("Enter perfect number or perfect square: ")
# # if x == "perfect_number":
# #     perfect_number(int(input("Enter a number: ")))  
# # elif x == "perfect_square":
# #     perfect_square(int(input("Enter a number: ")))
# # else:
# #     print("Invalid input. Please enter 'perfect_number' or 'perfect_square'.")

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



n=input('Enter item name :').split(',')
m = list(map(int, input('Enter item price:').split(',')))
def add_items(n,m):
    items={}
    for i in n:
        items[i]=m[n.index(i)]
    print(items)
    return items
    
def calculated_bill(cart):
    Total_bill=0
    Expensive_item=''
    cheaper_item=''     
    for item, price in cart.items():
        Total_bill+=int(price)
        if price == max(cart.values()):
            Expensive_item=f'{item} : {price}'
        elif price == min(cart.values()):
            cheaper_item=f'{item} : {price}'
    print(f'Most expensive item: {Expensive_item}')
    print(f'Cheapest item: {cheaper_item}')
    print(f'Total bill before discount: {Total_bill}')
    return Total_bill

def Discount(Total_Bill):
    if Total_Bill <= 10000:
        d1=Total_Bill*0.05
        print(f'you will get 5% Discount : {Total_Bill * 0.05}')
        return Total_Bill-(Total_Bill * 0.05)
    elif Total_Bill <= 20000:
        d2=Total_Bill*0.1
        print(f'you will get 10% Discount : {Total_Bill * 0.1}')
        return Total_Bill-(Total_Bill * 0.1)
    elif Total_Bill <= 29999:
        d3=Total_Bill*0.2
        print(f'you will get 20% Discount : {Total_Bill * 0.2}')
        return Total_Bill-(Total_Bill * 0.2)
    else:
        print(f'you will get 30% Discount : {Total_Bill * 0.3}')
        return Total_Bill-(Total_Bill * 0.3)
    
Cart_Items=add_items(n,m)
Total_Bill=calculated_bill(Cart_Items)
Final_Bill=Discount(Total_Bill)
print('--------------------------------------')
print('Final Bill After Discount:',Final_Bill)
print('--------------------------------------')