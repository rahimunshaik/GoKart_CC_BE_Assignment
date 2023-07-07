from tabulate import tabulate
from inventory import product_catalog,warehouse_catalog,customer_database,addProducts,addWarehouse,addStock,addState,viewState,processOrder,viewOrder,listProducts,listWarehouse,warehouseInfo

def display_catalog():
    product_headers=['Sku', 'Name','Category','Sub_category','Image_link']
    rows=[ [product['sku'],product['name'],product['category'],product['sub_category'],product['image_link']] for product in product_catalog ]
    print('Product Catalog:')
    print(tabulate(rows,product_headers,tablefmt='grid'))

    warehouse_headers=['Warehouse_id', 'Name','State','Location','Stock Limit']
    rows=[ [new_warehouse['warehouse_id'],new_warehouse['name'],new_warehouse['state'],new_warehouse['location'],new_warehouse['stock_limit']] for new_warehouse in warehouse_catalog ]
    print('Warehouse Catalog:')
    print(tabulate(rows,warehouse_headers,tablefmt='grid'))

   
    
    

while True:
    print(f"-------------------------------Welcome to GoKart Backend-------------------------------")
    command=input("Enter a command(ADD PRODUCT,ADD WAREHOUSE,ADD STOCK,ADD STATE,VIEW STATE,PROCESS ORDER, VIEW ORDERS,LIST PRODUCTS,LIST WAREHOUSE, WAREHOUSE INFO, DISPLAY CATALOG, QUIT):")
    if command == "QUIT":
        break
    elif command == "ADD PRODUCT":
        product_info=input("Enter product details(PRODUCT NAME, SKU, CATEGORY, SUB_CATEGORY, IMAGE_LINK):").split(',')
        if len(product_info) == 5:
            product_name, sku, category, sub_category, image_link =product_info
            addProducts(product_name, int(sku), category, sub_category, image_link)
        else:
            print("Invalid please enter valid data")
    elif command == "ADD WAREHOUSE":
                warehouse_id=input("Enter warehouse_id:-")
                name=input("Enter warehouse name:-")
                state=input("Enter state:-")
                latitude=float(input("Enter latitude:-"))
                longitude=float(input("Enter longitude:-"))
                location=(latitude,longitude)
                stock_limit=input("Enter Stock limit(optional)")
                addWarehouse(warehouse_id,name,state, location, stock_limit)
    elif command == "ADD STOCK":  
                sku=input("Enter Sku:-")        
                warehouse_id=input("Enter Warehouse ID:-")
                quantity=input("Enter Quantity:-")
                addStock(int(sku), warehouse_id, int(quantity))
    elif command == "ADD STATE":
                state=input("Enter State:-")
                addState(state)
    elif command == "VIEW STATE":
                 print("State Catalog")
                 viewState()
    elif command == "PROCESS ORDER":
        customer_id = input("Enter Customer ID:-")
        sku =input("Enter SKU:-")
        order_qty = int(input("Enter order quantity:-"))
        customer_location=input("Enter Customer Location(lat,lon):-")
        customer_location=tuple(float(coord) for coord in customer_location.split(','))

        processOrder(customer_id, sku, order_qty, customer_location)
        print(f"Process Order Successfull")

    elif command == "VIEW ORDERS":
        viewOrder()

    elif command == "LIST PRODUCTS":
        listProducts()
    
    elif command == "LIST WAREHOUSE":
        listWarehouse()
    elif command == " WAREHOUSE INFO":
        warehouseInfo()  

    elif command == "DISPLAY CATALOG":
        display_catalog()
    else:
        print("Invalid please try again")


