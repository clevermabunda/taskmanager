
import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost
    
    def get_code(self):
        
        return self.code

    def get_quantity(self):
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        pass
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

    def get_list(self):
        return[self.country, self.code, self.product, self.cost, self.quantity]
    
    def get_product(self):
        return self.product
    
    def get_country(self):
        return self.country
    


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''

shoe_list = []                 # Open an empty shoe list.


#==========Functions outside the class==============
def read_shoes_data():
    
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try :                                                 # Use try to avoid errors end crushing of the code.
        with open("inventory.txt", "r") as file:          
            file_content = file.readlines()[1:]           # Read the lines from index[1] to avoid error since headings are on index[0]
            for line in file_content:
                
                data = line.strip("\n").split(",")       # Avoid spliting with space because there is no space between data from the file
                shoe_list.append(Shoe(data[0], data[1], data[2], float(data[3]), int(data[4])))

    except FileNotFoundError:
        print ("The file don't exist, check if you have entered a correct file!!")
    except IndexError:
        print("The index you have entered is either out of range or incorrect!!!")



def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

    country = input("Please enter the name of the country: ")
    code = input("Please enter the shoe code: ")
    product = input("Please enter the name of the shoe you would like to order: ")
    cost = float(input("Please enter the price of the shoe:"))
    quantity = int(input("Please enter the amount of shoes you would like to order: "))
    shoe = Shoe(country, code, product, cost, quantity)

    shoe_list.append(shoe)                        # Append the shoe data in an empty shoe_list file.

    with open("inventory.txt", "a+") as file:
        file.write(f"{country}, {code}, {product}, {cost}, {quantity}\n")   



def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    

    shoe_table_data = [shoe.get_list() for shoe in shoe_list]
    print("\n\t\t\tTABLE : ")
    print(tabulate.tabulate(shoe_table_data, headers=["Country", "Code", "Product", "Cost", "Quantity"],tablefmt="grid"))

def re_stock():
    pass
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    table = []

    shoe_list.sort(key=lambda x:x.quantity)          # Sort the data using the key=lambda.

    for i in range(1,6):
        restock_list.append(shoe_list[i])

    print ("\n\t\t\tLowest stock items :\n".upper())  


    for line in restock_list:
        country.append(line.get_country())
        code.append(line.get_code())
        product.append(line.get_product())
        cost.append(line.get_cost())
        quantity.append(line.get_quantity())

    table = zip(country, code, product, cost, quantity)
    print(tabulate.tabulate(table, headers = ('Country','Code', 'Product', 'Cost', 'Quantity'), tablefmt='grid', showindex= range(1,6)))
    
    choice = int(input("\nUsing index number,please enter the correct index number to restock:"))
    stock = int(input("\nPlease enter the amount of stock like to order:"))
    shoe_list[choice].quantity += stock
    print (shoe_list[choice].quantity)

    with open("inventory.txt", "w") as file:
        file.write("Country, Code, Product, Cost, Quantity")
        for shoes in range(len(shoe_list)):
            file.write(f"{shoe_list[shoes].country}, {shoe_list[shoes].code}, {shoe_list[shoes].product}, {shoe_list[shoes].cost}, {shoe_list[shoes].quantity}\n")
    print ("You have successfully added your stock!\n")                 
        
    

def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    search = input("Please enter the code of the you are looking for: ").upper()
    for i in shoe_list:
        if i.get_code() == search:
            print(i)


def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
   
    for line in shoe_list:
        value = int(line.get_cost()) * int(line.get_quantity())
        print (f"\n{line.get_code()} R{value}\n")

                
                          
def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if shoe_list:
        print(max(shoe_list, key=lambda x: x.quantity))         # Use key=lambda to find the maximum quantity
        print("ON SALE!!!!!!")

    else:
        print("no shoes")
            

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()
while True:
     print(''' \n\t\tMain Menu
           1. view all
           2. restock
           3. capture shoes
           4. search shoe
           5. value per item
           6. highest qty
           7. exit''')
     selection = int(input("\nEnter your menu selection using a corresponding number: "))
     if selection == 1:
        view_all()
     elif selection == 2:
        re_stock()
     elif selection == 3:
        capture_shoes()
     elif selection == 4:
        seach_shoe()
     elif selection == 5:
        value_per_item()
     elif selection == 6:
        highest_qty()
     elif selection == 7:
        print("Goodbye!")
        break
     else:
        print("\nYou have an incorrect number, please try again!!.")
    