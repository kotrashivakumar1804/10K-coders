class Product:
    def __init__(self,id,name,price,rating):
        self.id=id
        self.name=name
        self.price=price
        self.rating=rating
class User:
    def __init__(self):
        self.products=[]
    def add_product(self):
        id=int(input('enter product id:'))
        for product in self.products:
            if product.id == id:
                print('product id already exists')
                print('-'*50)
                return
        name=input('enter product name:')
        if len(name) <= 7:
            name += ' ' * (7-len(name))
        price=float(input('enter product price:'))
        rating=float(input('enter product rating:'))
        product=Product(id,name,price,rating)
        self.products.append(product)
        print('product added successfully to the cart.....!')
        print('-'*50)

    def remove_product(self):
        if(len(self.products) == 0):
            print('cart is empty.....!')
            return
        id=int(input('enter product id to remove:'))
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print('product removed successfully from the cart.....!')
                print('-'*50)
                return
        print('product not found in the cart.....!')
        print('-'*50)

    def Update_product(self):
        if(len(self.products) == 0):
            print('cart is empty.....!')
            return
        id=int(input('Enter product id to update:'))
        for product in self.products:
            if product.id == id:
                while True:
                    print('SELECT 1 -->update name')
                    print('SELECT 2 -->update price')
                    print('SELECT 3 -->update rating')
                    print('SELECT 4 -->update all') 
                    print('SELECT 5 -->save the changes and exit')
                    print('-'*50)
                    choice=int(input('Enter your choice:'))
                    print('-'*50)
                    match choice:
                        case 1:
                            name=input('Enter new product name:')
                            product.name=name
                            print('product name updated successfully.....!')
                        case 2:
                            price=float(input('Enter new product price:'))
                            product.price=price
                            print('product price updated successfully.....!')   
                        case 3:   
                            rating=float(input('Enter new product rating:'))
                            product.rating=rating
                            print('product rating updated successfully.....!')          
                        case 4:
                            name=input('Enter new product name:')
                            price=float(input('Enter new product price:'))
                            rating=float(input('Enter new product rating:'))
                            product.name=name
                            product.price=price
                            product.rating=rating
                            print('product details updated successfully.....!') 
                        case 5:
                            print('changes saved successfully.....!')
                            return
                        case _:
                            print('invalid choice.....!')
        print('product not found in the cart.....!')
        print('-'*50)

    def show_products(self):
        if (len(self.products) == 0):
            print('cart is empty.....!')
            return
        print('-'*40)
        print(' | ID | Name   | Price | Rating |')
        print('-'*40)
        for product in self.products:
            print(f' | {product.id} | {product.name} | {product.price} | {product.rating} |')
        print('-'*40)

    def search_product(self):
        if (len(self.products) == 0):
            print('cart is empty.....!')
            return
        print('-'*50)
        print('1 ---> search with id')
        print('2 ---> search with name')
        print('-'*50)
        choice=int(input('Enter your choice:'))
        print('-'*50)
        if choice == 1:
            id=int(input('Enter product id to search:'))
            for product in self.products:   
                if product.id == id:
                    print('-'*40)
                    print(' | ID | Name   | Price | Rating |')
                    print('-'*40)
                    print(f' | {product.id} | {product.name} | {product.price} | {product.rating} |')
                    print('-'*40)
                    print('-'*50)
                    return
            print('product not found in the cart.....!')
            print('-'*50)
        elif choice == 2:
            name=input('Enter product name to search:')
            for product in self.products:
                if len(name) <= 7:
                    name += ' ' * (7-len(name))
                if product.name == name:
                    print('-'*40)
                    print(' | ID | Name   | Price | Rating |')
                    print('-'*40)
                    print(f' | {product.id} | {product.name} | {product.price} | {product.rating} |')
                    print('-'*40)
                    print('-'*50)
                    return
            print('product not found in the cart.....!')
            print('-'*50)

    def sort_price(self):
        if (len(self.products) == 0):
            print('No products in the cart.....!')
            return
        self.products.sort(key=lambda x: x.price, reverse=False)
        print('products sorted by price in ascending order.....!')
        print('-'*50)

    def sort_rating(self):
        if (len(self.products) == 0):
            print('No products in the cart.....!')
            return
        self.products.sort(key=lambda x: x.rating, reverse=True)
        print('products sorted by rating in descending order.....!')
        print('-'*50)
        
print('......$ Welcome to the Product Management System $......')
print('-'*50)
user=User()
while True:
    print('SELECT 1 -->Add product to the cart')
    print('SELECT 2 -->Remove product from the cart')
    print('SELECT 3 -->Update product details')
    print('SELECT 4 -->Show all products in the cart')
    print('SELECT 5 -->Search product in the cart')
    print('SELECT 6 -->Sort products by price')
    print('SELECT 7 -->Sort products by rating')
    print('SELECT 8 -->save and Exit')
    print('-'*50)
    choice=int(input('Enter your choice:'))
    print('-'*50)
    match choice:
        case 1: user.add_product()
        case 2: user.remove_product()
        case 3: user.Update_product()
        case 4: user.show_products()
        case 5: user.search_product()
        case 6: user.sort_price()
        case 7: user.sort_rating()
        case 8:
            print('Thank you for using the Product Management System. Goodbye!')
            break
        case _:
            print('Invalid choice. Please try again.')
            print('-'*50)