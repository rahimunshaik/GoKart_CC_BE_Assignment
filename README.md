# GoKart_CC_BE_Assignment
I have made a simple command line project using Python with the help of vs code just follow the below steps to overview the experience :)

## GoKart Inventory Management
This project provides a command line REPL (Read-Eval-Print Loop) for managing product inventory in GoKart, a quick commerce start-up. 
The inventory management system allows you to add products to the catalog, add warehouses to store the products, process orders, and 
perform various operations related to inventory management.

## Installation
Clone the repository:

git clone https://github.com/your-username/GoKartInventoryManagement.git

#Change into the project directory:

cd GoKartInventoryManagement

#Install the required dependencies:
pip install tabulate

## Usage
Run the program:
python manage_inventory.py

Use the command line REPL to interact with the inventory management system. Enter the commands as instructed to perform various operations, such as adding products, warehouses, processing orders, and viewing inventory details.

To quit the program, enter "QUIT" in the command line REPL.

##Command List
The following commands are available for managing the product inventory:

ADD PRODUCT - Add a new product to the product catalog.
ADD WAREHOUSE - Add a new warehouse to store the products.
ADD STOCK - Add stock quantity to a specific product in a warehouse.
ADD STATE - Add a new state where GoKart operates.
VIEW STATE - View the list of states along with the number of warehouses and total stock capacity in each state.
PROCESS ORDER - Process an order for a customer and fulfill it from the nearest warehouse.
VIEW ORDERS - View the list of orders punched in the system along with customer ID, order date, fulfillment status, and linked warehouse.
LIST PRODUCTS - List all products in the product catalog along with the current stock quantity and in-stock warehouses.
LIST WAREHOUSES - List all warehouses along with the warehouse ID, state, and location (latitude, longitude).
WAREHOUSE INFO - View information about a specific warehouse, including the available SKUs, warehouse ID, and available storage.

##Developer 
Shaik Rahimun



