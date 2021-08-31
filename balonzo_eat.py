# Create resturant class

class restaurant:
    def __init__(self, menu, customers, order):
        self.menu = menu 
        self.customers = customers
        self.order = order 


# Create a  menu
menu = ["burger", "steak", "Veggies", "Soda"]

# Menu: create a dictionary for menu

# Menu: should have names and prices

# MENU: add item to menu 

# Menu: Should remove item from menu

# Menu: item prices changed



# Create a customer
customer = {
    "Name": "Lucas Santos",
    "cell": "6012544889",
}

# Customer: name for cutomer

# Customer: contact info phone or email

# Customer: available funds so we can afford items.
wallet = 100

if order == "burger":
    remainder = wallet - 12
    print(f"You now have {remainder}")    


if order == "steak":
    remainder = wallet - 15
    print(f'You now have {remainder}')


if order == "veggies":
    remainder = wallet - 20
    print(f"You now have ${remainder}")


if order == "soda":
    remainder = wallet - 4
    print(f"You now have ${remainder}")


# Create an order

# Order: name for order

# Order: items on the order

# Order; status of the order

# Order: checkout complete order based on customer info

# create input









