from Menu import print_menu, print_header
from Item import Item
import os
import pickle

catalog = []
id_count = 1
data_file = "catalog.data"

# method declarations

def clear():
    return os.system('clear')

def save_catalog():
    global data_file
    writer = open(data_file, "wb")
    pickle.dump(catalog, writer)
    writer.close()
    print('Data Saved!!')

def read_catalog():
    global data_file
    global id_count
    
    try:
        reader = open(data_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]   
        id_count = last.id + 1 
    
        how_many = len(catalog)
        print(" Loaded " + str(how_many) + "Items")
    except: 
        print("Error loading data")    
 
def register_item():
    global id_count
    print_header(' Register new Item ')
    title = input('Please input Title: ')
    category = input('Please input Category: ')
    price =float(input('Please input Price: '))
    stock = int(input('Please input Stock: '))

    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    id_count += 1
    catalog.append(new_item)
    print(" Item created!")

def display_catalog():
    num_items = len(catalog)
    print_header(' Your catalog contains ' + str(num_items) + ' Items ')
    print(' |ID   |  Title                 | Category           |      Price  | Stock     ]')
    print('-' * 80)
   
    for item in catalog:
        print(item.title.ljust(20) 
        + " | " + item.category.ljust(15) 
        + " | " + str(item.price).rjust(9) 
        + " | " + str(item.stock).rjust(5) )
   
    print('-' * 80)

def display_no_stock(): 
    print_header('Item out of stock')
    print('  Title                 | Category           |      Price  | Stock     ]')
    print('-' * 80)
   
    for item in catalog:
        if(item.stock == 0):
             print("|" + str(item.id).ljust(3) +
             " | " + item.title.ljust(20) 
             + " | " + item.category.ljust(15) 
             + " | " + str(item.price).rjust(9) 
             + " | " + str(item.stock).rjust(5) )
   
    print('-' * 80)
 
def update_stock():
    display_catalog
    selected = int(input('Please select the ID to update: '))

    found = False
    for item in catalog:
        if(item.id == selected):
            new_stock = input(' Please input new stock value: ')
            item.stock = int(new_stock)
            found = True
            print(' Stock updated!!')

    if(found == False):
        print('** Error: Selected ID does not exist, try again')  

def print_stock_value():
    print_header(" Current Stock Value")
    
    total = 0.0
    for item in catalog:
        total += (item.price * item.stock)  

    print('Total value: ' + str(total))  

def remove_item():
    display_catalog() 
    remove_id = int(input("Please select the ID to remove: "))
    
    found = False
    for item in catalog:
        if(item.id == remove_id):
           
           found = True
           catalog.remove(item)

    if(not found):
        print("*Error, wrong Id, try again!")   


def list_categories():
    print_header("List of categories used on the system")
    already_printed = []
    for item in catalog:
        if not item.category in already_printed:
            print(item.category)
            already_printed.append(item.category)           

read_catalog()

# loop display menu 
opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Select an option: ')

    if(opc == '1'):
        register_item()
        save_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_no_stock()  
    elif(opc == '4'):
        update_stock() 
        save_catalog()
    elif(opc == '5'):
        print_stock_value()  
    elif(opc == '6'):
        remove_item()           
        save_catalog()
    elif(opc == '7'):
        list_categories()    
    
    input('Press Enter to continue...')            