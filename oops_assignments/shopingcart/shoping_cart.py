'''the  class give  functions to add catalogues,and add items to cart,also manage it'''

class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f'Product id: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}'


class UserFunctions:#give funciton to user roles
    def __init__(self):
        self.cart = list()

    def add_cart(self, product):
        print(product)
        self.cart.append(product)
        print("Product added to cart")

    def delete_cart(self, product_id):
        for i in range(len(self.cart)):
            if self.cart[i].product_id == product_id:
                self.cart.pop(i)
                print("Product deleted successfully!")
                return
        print("No item found with the given product id")

    def display_cart(self):
        if len(self.cart) == 0:
            print("No Items Found")
        else:
            for i, product in enumerate(self.cart, 1):
                print(f"Product {i}: {product}")


class AdminFunctions:#give functions to admin roles
    def __init__(self):
        self.item_storage = list()

    def add_item(self, product):
        self.item_storage.append(product)
        print("Product added")

    def update_item(self, product_id, new_product):
        for i in range(len(self.item_storage)):
            if self.item_storage[i].product_id == product_id:
                self.item_storage[i] = new_product
                print("Product updated successfully")
                return
        print("No item found with the given product id")

    def delete_item(self, product_id):
        for i in range(len(self.item_storage)):
            if self.item_storage[i].product_id == product_id:
                self.item_storage.pop(i)
                print("Product deleted successfully!")
                return
        print("No item found with the given product id")

    def display_item(self):
        if len(self.item_storage) == 0:
            print("No Items Found")
        else:
            for i, product in enumerate(self.item_storage, 1):
                print(f"Product {i}: {product}")

    def return_catalog(self):
        return self.item_storage


class Authentication:#specifies admin and user roles according to given passwords
    user_db = {"user": "user", "user1": "user1"}
    admin_db = {"admin": "admin"}

    def user_login(self, username, password):
        if username in self.user_db:
            if self.user_db[username] == password:
                print(f"\nLogin Successful \n Welcome user {username} \n")
                usercli()
            else:
                print("\n Wrong Password \n")
        else:
            print('\n Wrong username')

    def admin_login(self, username, password):
        if username in self.admin_db:
            if self.admin_db[username] == password:
                print(f"\n Welcome Admin {username} \n")
                admincli()
            else:
                print("\n Wrong Password \n")
        else:
            print('\n Wrong username')


import random

def generate_session_id():
    return random.randint(10000, 100000)


f = AdminFunctions()

def admincli():
    session_id = generate_session_id()
    print(f"Admin session id is {session_id}")

    while True:
        choice = input("Select a Choice \n 1. Add item \n 2. Update \n 3. Delete \n 4. Display Catalog \n 6. Log Out \n ")
        if choice == '1':
            print("\n Enter the details of item \n")
            product_id = int(input("Enter unique id for item: "))
            name = input("Enter the name of the product: ")
            category = input("Enter the category: ")
            price = int(input("Enter the price: "))

            obj1 = Product(product_id, name, category, price)
            f.add_item(obj1)
        elif choice == '2':
            print("\n Enter the details of the updated item \n")
            product_id = int(input("Enter unique id of item to be updated: "))
            new_product_id = int(input("Enter the new unique id of item: "))
            name = input("Enter the name: ")
            category = input("Enter the Category: ")
            price = int(input("Enter the price: "))

            obj2 = Product(new_product_id, name, category, price)
            f.update_item(product_id, obj2)
        elif choice == '3':
            e_id = int(input("Enter the product id for deleting item: "))
            f.delete_item(e_id)
        elif choice == '4':
            print('\n Current Catalog is \n')
            f.display_item()
        elif choice == '6':
            print("\n Thank you for using our service! Logging Out... \n")
            break
        else:
            print("\n Wrong Choice \n")


def usercli():
    session_id = generate_session_id()
    print(f"User session id is {session_id}")

    f1 = UserFunctions()

    while True:
        choice = input("Select a Choice \n 1. Add to cart \n 2. Delete from cart \n 3. Display Cart \n 4. Display Catalog \n 5. Check Out \n 6. Log out \n ")
        if choice == '1':
            print("\n Select The item to be added \n")
            cart1 = f.return_catalog()

            if not cart1:
                print("No items available in the catalog.")
                continue

            for i, product in enumerate(cart1, 1):
                print(f"Product {i}: {product}")

            try:
                p = int(input("Select the item number: "))
                if 1 <= p <= len(cart1):
                    item1 = cart1[p - 1]
                    f1.add_cart(item1)
                else:
                    print("Invalid item number selected.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            f1.display_cart()
            try:
                e_id = int(input("Enter the product id to be deleted from cart: "))
                f1.delete_cart(e_id)
            except ValueError:
                print("Please enter a valid product id.")
        
        elif choice == '3':
            print("\nThe current cart is:\n")
            f1.display_cart()
        
        elif choice == '4':
            print("\n The available products are:\n")
            cart1 = f.return_catalog()

            if not cart1:
                print("No items available in the catalog.")
                continue

            for i, product in enumerate(cart1, 1):
                print(f"Product {i}: {product}")
        
        elif choice == '5':
            payment_method = input("Enter the payment method (Debit/Credit): ")
            print(f"\n{payment_method} payment successful \n Redirecting ....")
        
        elif choice == '6':
            print("Logging out ...")
            break
        
        else:
            print("\n Wrong Choice \n")



def main():
    print("\n Welcome to Demo marketplace \n")
    while True:
        choice = input("1. Login 2. Exit ")
        if choice == '1':
            print("\n User Authentication \n")
            user_type = int(input("Choose \n 1 for user \n 2 for admin \n"))
            name = input("Enter the username: ")
            password = input("Enter the password: ")
            u = Authentication()
            if user_type == 1:
                u.user_login(name, password)
            elif user_type == 2:
                u.admin_login(name, password)
        else:
            break

if __name__ == "__main__":
    main()
