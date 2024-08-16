'''this project involves Exepense tarcker for adding,managing and delting expenses '''
class Expense:
    def __init__(self,expense_id,date,category,description,amount):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.description = description 
        self.amount = amount

    def __str__(self):
        return f'Expense id is {self.expense_id} \n date of expense is {self.date} \n Category is {self.category} \n Description is {self.description} \n Amount of expenditrue {self.amount}'

class Calc:#this contains methodds for add,update and delete expenses

    def __init__(self):

        self.expense_storage = list()

  
    def add_expenses(self,expense):
        self.expense_storage.append(expense)
        print("Expense added")
    
    def update_expense(self,expense_id,new_expense):
        for i in range(len(self.expense_storage)):
            if self.expense_storage[i].expense_id == expense_id:
                self.expense_storage[i] = new_expense
                print("Expense updated successfully ")
                return
        print("NO iterm found with expense id")
    
    def delete_expense(self,expense_id):
        for i in range(len(self.expense_storage)):
            if self.expense_storage[i].expense_id == expense_id:
                self.expense_storage.remove(self.expense_storage[i])
                print("Expense delted successfully! ")
                return
        print("No item found with expense id")
        
    

    def display_expense(self):
        for i in range(len(self.expense_storage)):
            print(str(self.expense_storage[i]))
        if len(self.expense_storage) == 0:
            print("No Items Found")
    
    def categorize_expenses(self):
        category_dictionary =dict()
        for i in range(len(self.expense_storage)):
            if self.expense_storage[i].category in category_dictionary:
                category_dictionary[self.expense_storage[i].category] += self.expense_storage[i].amount
            else:
                category_dictionary[self.expense_storage[i].category] = self.expense_storage[i].amount
        return category_dictionary

    def summarize_expense(self):
        total=0
        for i in range(len(self.expense_storage)):
            total+=self.expense_storage[i].amount
        return total
    
    def calculate_total_expense(self):
        total_sum = sum(x.amount for x in self.expense_storage)
        return total_sum
    
    def generate_summary_report(self):
        #to get expense in each category
        d=self.categorize_expenses()
        print(d)
        for i ,j in d.items():
            print(f"Category : {i} Total Expenses : {j}")
        total_expense= self.summarize_expense()
        print("Total Expense",total_expense)


    #it authenticates role of users

class Aunthetication:
    user_dict={"user":"user","user1":"user1"}
    def authenticate_user(self,username,password):
        if username in self.user_dict:
            if self.user_dict[username] == password:
                return True
            else:
                return False
        else:
            return False
        


def cli():

    f = Calc()
   
    while True:
        choice=input("Select a Choice \n 1. Add item \n 2. Update \n 3 . Delete \n 4. Display Expense \n 5 . Generate Summary report \n 6. Exit \n ")
        if choice == '1':
            print("\n Enter the details of expense \n")
            expesne_id = int(input("Enter unique id for expense : "))
            date = input("Enter the date : ")
            category = input("Enter the Category : ")
            desc = input("Enter the description : ")
            amount = int(input("Enter the amount of expenditure"))

            obj1=Expense(expesne_id,date,category,desc,amount)
           

            
            f.add_expenses(obj1)
        elif choice == '2':
            print("\n Enter the details of the updated expense \n")
            expesne_id = int(input("Enter unique id for expense : "))
            new_expensense_id =int(input("Enter the new unique id for expense : "))
            date = input("Enter the date : ")
            category = input("Enter the Category : ")
            desc = input("Enter the description : ")
            amount = int(input("Enter the amount of expenditure"))

            obj2=Expense(new_expensense_id,date,category,desc,amount)
            f.update_expense(expesne_id,obj2)

        elif choice == '3':
            print("\n Enter the expense id for deleting Expense : ")
            e_id = int(input("Enter the expense id for deleting Expense : "))
            f.delete_expense(e_id)

        elif choice == '4':
            f.display_expense()
        
        elif choice == '5':
            f.generate_summary_report()
        
        elif choice == '6':
            print("\n Thank you for using our service ! \n")
            break

        else:
            print("\n Wrong Choice \n")
        







def main():
    print("\n Welcome to expense tracker \n")

    print("\n User Authentication \n")
    name = input("Enter the user name : ")
    password =input("Enter the password : ")
    u = Aunthetication()
    if u.authenticate_user(name,password):
        print("Login Successful")
        cli()
    else:
        print("\n Wrong credentials Please try aNgain \n")
    
if __name__ == "__main__":
    main()
        


            

        
    



                



