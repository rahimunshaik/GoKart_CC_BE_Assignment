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

## Command List
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

## PRODUCT AND WAREHOUSE CATALOG:-
https://github-production-user-asset-6210df.s3.amazonaws.com/88622657/251939348-5b11dc99-f6b4-4c9b-8a06-95b4a14525f2.png

## VIEW STATE 
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/d355dd2e-18e9-47b5-89ec-2fd439faf02f

## VIEW ORDERS
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/04dc9b4a-a3c1-4293-bf94-168fc59fa5ae

## LIST PRODUCTS
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/d35799b2-146f-4c11-bec2-b9781046d09A

## LIST WAREHOUSE
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/6dff4a76-a8a2-402d-b3a2-9701ae9cc5c1



=========================================================================================================
Questions about my assignment
6. How would you go about the development of this project in real life?

Your plan should touch on the following aspects:
- How will you do CI/CD?
- What cloud resources are required for the running of this project? Delineate the steps you would take for deployment. Assume 10k monthly users with 500 transactions a day for this purpose.
- What tools would you use to test & monitor the deployment? 

Substantiate your answers with some reasoning 
Reason: I want my application to be fast, easy to use, and understandable while reducing errors and enabling continuous monitoring. CI/CD helps streamline the deployment and development process.

To achieve continuous integration and continuous deployment, I implemented the following:

Version Control: Used Git to manage code and collaborate with the development team in the future.
Continuous Integration: Automatically builds and tests the application whenever changes are added through Git.
Monitoring and Continuous Deployment: These aspects also play a significant role in the development process.
7.Now assume that you have to deploy your code for production. 

What are the unit, functional & integrity tests that you will write in order to test the integrity of the code base
What would be the success criteria for the backend & how will you measure them objectively?
Please share a HLD, DB schema & API schema for the codebase (you can add a link to a pdf/img file or upload this directly in the github repo itself)


Substantiate your answers with some reasoning 
1. The unit, Functional and integrity tests that I have written in order to test the integrity of the code base are :--

1.1 Unit Tests:

1.1.1 Product Catalog Unit Tests:

Test adding a new product to the catalog.
Test adding a product with an existing SKU.
Test retrieving product information by SKU.

1.1.2 Warehouse Catalog Unit Tests:

Test adding a new warehouse to the catalog.
Test adding a warehouse with an existing ID.
Test retrieving warehouse information by ID.

1.1.3 Stock Management Unit Tests:

Test adding stock to a warehouse.
Test adding stock for a non-existent product SKU.
Test adding stock for a non-existent warehouse ID.

1.2 Functional Tests:

1.2.1 Add Product Functionality Test:

Test the functionality of adding a product to the catalog.

1.2.2 Add Warehouse Functionality Test:

Test the functionality of adding a warehouse to the catalog.

1.2.3 Add Stock Functionality Test:

Test the functionality of adding stock to a warehouse.

1.2.4 Process Order Functionality Test:

Test the functionality of processing an order.

1.3 Integrity Tests:

1.3.1 Product Catalog Integrity Test:

Check that all products in the catalog have unique SKUs.
Verify that all SKUs are integers.

1.3.2 Warehouse Catalog Integrity Test:

Check that all warehouses in the catalog have unique IDs.
Verify that all IDs follow the specified format (6-digit string).

1.3.3 Stock Management Integrity Test:

Verify that stock quantities are positive integers.
Check that stock quantities do not exceed the stock limit (if defined) for a warehouse.


2. Success Criteria for the Backend:

All unit tests pass without any failures or errors.
Functional tests demonstrate the correct behavior of each feature.
Integrity tests ensure that data is consistent and follows the specified rules.
The application operates smoothly without any critical errors or crashes.
Adequate error handling and validation are in place to prevent unexpected behavior.
Objective Measurement:

Unit tests provide a quantifiable measure of the code's correctness by checking individual components and functions.
Functional tests evaluate the overall functionality of the application by simulating user interactions and verifying expected outcomes.
Integrity tests ensure that the data and business rules are maintained properly.
Monitoring tools and logs can be utilized to track any backend errors, exceptions, or performance issues.
Regular performance testing can be conducted to measure response times, throughput, and scalability of the backend system.


3.  HLD, DB schema & API schema for my codebase:-

## PRODUCT AND WAREHOUSE CATALOG:-
https://github-production-user-asset-6210df.s3.amazonaws.com/88622657/251939348-5b11dc99-f6b4-4c9b-8a06-95b4a14525f2.png

## VIEW STATE 
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/d355dd2e-18e9-47b5-89ec-2fd439faf02f

## VIEW ORDERS
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/04dc9b4a-a3c1-4293-bf94-168fc59fa5ae

## LIST PRODUCTS
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/d35799b2-146f-4c11-bec2-b9781046d09A

## LIST WAREHOUSE
https://github.com/rahimunshaik/GoKart_CC_BE_Assignment/assets/88622657/6dff4a76-a8a2-402d-b3a2-9701ae9cc5c1

8.What is the coolest piece of tech you have come across? What made it so cool?

Honestly, more than gadgets, I use software tools mostly, including AI tools. I like to explore much in tech, and AI is awesome. I have gone through Scribble Diffusion as I am fascinated by fantasies and painting. I like this AI tool very much, and it's free of cost. You can also have a look at it. Here is the link: https://scribblediffusion.com/

9.What is the project you have worked on & are most proud of? How was your experience and what made it so special?

This need not even be a tech project.
While I was in college, I worked on a minor project called "Automatic Bill Generation and Business Insights." Initially, as a team, we were challenged by the COVID situation, so we decided to create a crowd-free billing system to help in such situations. It was our own idea, which we implemented in our minor project. However, the unfortunate part is that we didn't save our project and the data we collected because we were unaware of GitHub and similar technologies at that time. Nevertheless, it was my first project, and each one of us was very proud of the idea that aimed to reduce the crowd at the billing system, which made it even more special.




##Developer 
Shaik Rahimun



