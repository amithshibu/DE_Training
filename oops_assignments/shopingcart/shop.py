# Class representing a product in the marketplace
class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id  # Unique identifier for the product
        self.name = name  # Name of the product
        self.category = category  # Category to which the product belongs
        self.price = price  # Price of the product

    def __str__(self):
        # String representation of the product
        return f'Product ID: {self.product_id}\nName: {self.name}\nCategory: {self.category}\nPrice: {self.price}'


# Class representing user-related operations like adding to cart, deleting from cart, etc.
class UserFunctions:

    def __init__(self):
        self.cart = []  # Initialize an empty cart for the user

    def add_cart(self, product):
        print(product)  # Display the product being added to the cart
        self.cart.append(product)  # Add the product to the cart
        print("Product added to cart")

    def delete_cart(self, product_id):
        # Loop through the cart to find and remove the product with the specified product_id
        for i in range(len(self.cart)):
            if self.cart[i]['product_id'] == product_id:
                self.cart.remove(self.cart[i])
                print("Product deleted successfully from cart!")
                return
        print("No item found with the specified product ID")

    def display_cart(self):
        # Display the contents of the cart
        for i in range(len(self.cart)):
            print(f"Product {i}: {self.cart[i]}")
        if len(self.cart) == 0:
            print("No items in the cart")


# Class representing admin-related operations like adding, updating, deleting products in the catalog
class AdminFunctions:

    def __init__(self):
        self.item_storage = []  # Initialize an empty list to store products

    def add_item(self, product):
        item = vars(product)  # Convert the product object to a dictionary
        self.item_storage.append(item)  # Add the product to the storage
        print("Product added to catalog")

    def update_item(self, product_id, new_product):
        d = vars(new_product)  # Convert the updated product object to a dictionary
        # Loop through the item storage to find and update the product with the specified product_id
        for i in range(len(self.item_storage)):
            if self.item_storage[i]['product_id'] == product_id:
                self.item_storage[i] = d
                print("Product updated successfully")
                return
        print("No item found with the specified product ID")

    def delete_item(self, product_id):
        # Loop through the item storage to find and delete the product with the specified product_id
        for i in range(len(self.item_storage)):
            if self.item_storage[i]['product_id'] == product_id:
                self.item_storage.remove(self.item_storage[i])
                print("Product deleted successfully!")
                return
        print("No item found with the specified product ID")

    def display_item(self):
        # Display the contents of the item storage (catalog)
        for i in range(len(self.item_storage)):
            print(f"Product {i+1}: {self.item_storage[i]}")
        if len(self.item_storage) == 0:
            print("No items found in the catalog")

    def return_catalog(self):
        # Return the entire catalog of items
        return self.item_storage


# Class representing user and admin authentication functionality
class Authentication:
    user_db = {"user": "user", "user1": "user1"}  # Sample user database
    admin_db = {"admin": "admin"}  # Sample admin database

    def user_login(self, username, password):
        # Authenticate the user
        if username in self.user_db:
            if self.user_db[username] == password:
                print(f"\nLogin Successful\nWelcome, user {username}\n")
                usercli()
            else:
                print("\nWrong Password\n")
        else:
            print('\nWrong username')

    def admin_login(self, username, password):
        # Authenticate the admin
        if username in self.admin_db:
            if self.admin_db[username] == password:
                print(f"\nWelcome, Admin {username}\n")
                admincli()
            else:
                print("\nWrong Password\n")
        else:
            print('\nWrong username')


# Generate a random session ID for user or admin sessions
import random
def generate_session_id():
    return random.randint(10000, 100000)


# Command-line interface for admin functions
def admincli():
    session_id = generate_session_id()
    print(f"Admin session ID is {session_id}")

    while True:
        choice = input("Select an option:\n1. Add item\n2. Update item\n3. Delete item\n4. Display catalog\n6. Log Out\n")
        if choice == '1':
            print("\nEnter the details of the item\n")
            product_id = int(input("Enter unique product ID: "))
            name = input("Enter the name of the product: ")
            category = input("Enter the category: ")
            price = int(input("Enter the price: "))

            obj1 = Product(product_id, name, category, price)
            f.add_item(obj1)
        elif choice == '2':
            print("\nEnter the details of the updated item\n")
            product_id = int(input("Enter the product ID to be updated: "))
            new_product_id = int(input("Enter the new unique product ID: "))
            name = input("Enter the name: ")
            category = input("Enter the category: ")
            price = int(input("Enter the price: "))

            obj2 = Product(new_product_id, name, category, price)
            f.update_item(product_id, obj2)
        elif choice == '3':
            print("\nEnter the product ID to be deleted: ")
            e_id = int(input("Enter the product ID to be deleted: "))
            f.delete_item(e_id)
        elif choice == '4':
            print('\nCurrent catalog:\n')
            f.display_item()
        elif choice == '6':
            print("\nThank you for using our service. Logging Out!\n")
            break
        else:
            print("\nInvalid choice\n")


# Command-line interface for user functions
def usercli():
    session_id = generate_session_id()
    print(f"User session ID is {session_id}")

    f1 = UserFunctions()
    while True:
        choice = input("Select an option:\n1. Add to cart\n2. Delete from cart\n3. Display cart\n4. Display catalog\n5. Check Out\n6. Log Out\n")
        if choice == '1':
            print("\nSelect the item to be added to the cart\n")
            cart1 = f.return_catalog()
            for i in range(len(cart1)):
                print(f"Product {i}: {cart1[i]}")
            p = int(input("Select the item number: "))

            item1 = cart1[p]
            f1.add_cart(item1)
        elif choice == '2':
            f1.display_cart()
            print("\nEnter the product ID to delete from cart: ")
            e_id = int(input("Enter the product ID: "))
            f1.delete_cart(e_id)
        elif choice == '3':
            print("\nThe current cart is:\n")
            f1.display_cart()
        elif choice == '4':
            print("\nThe available products are:\n")
            cart = f.return_catalog()
            for i in range(len(cart)):
                print(f"Product {i}: {cart[i]}")
        elif choice == '5':
            payment_method = input("Enter the payment method:\nDebit\nCredit\n")
            print(f"\n{payment_method} payment successful. Redirecting...\n")
        elif choice == '6':
            print("Logging out...")
            break
        else:
            print("\nInvalid choice\n")


# Main function to start the application
def main():
    print("\nWelcome to Demo Marketplace\n")
    while True:
        choice = input("1. Login\n2. Exit\n")
        if choice == '1':
            print("\nUser Authentication\n")
            user_type = int(input("Choose:\n1 for user\n2 for admin\n"))
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
