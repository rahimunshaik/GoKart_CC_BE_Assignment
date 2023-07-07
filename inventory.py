import math
from tabulate import tabulate 

# Command -1 ADD Products
product_catalog=[
    {
        'name': 'Santoor',
        'sku':1,
        'category':'Cleaning',
        'sub_category': 'Soap',
        'image_link':'image1.png',

    },
    {
        'name': 'oliv oil',
        'sku':2,
        'category':'Beauty',
        'sub_category': 'Oil',
        'image_link':'image2.png',

    }
]

# Command -2 ADD Warehouse

warehouse_catalog=[
    {
        'warehouse_id': '01',
        'name':'warehouse 1',
        'state':'AP',
        'location': (31.22,45.54),
        'stock_limit':100,

    },
    {
        'warehouse_id': '02',
        'name': 'warehouse 2',
        'state':'Kerala',
        'location': (11.22,50.54),
        'stock_limit':10,

    }
    
]

customer_database =[
    {
        'customer_id': 'CUST01',
        'name': 'Rose',
        'location': (12.34,34.45)
    },
    {
        'customer_id': 'CUST02',
        'name': 'Jack',
        'location': (11.34,33.45)
    },
]


order_database =[
    {
        'order_id':'ORD01',
        'customer_id': 'CUST01',
        'order_date': '23-4-23',
        'fullfilment_status': 'Pending',
        'warehouse_id':'01'
    },
    {
        'order_id':'ORD02',
        'customer_id': 'CUST02',
        'order_date': '24-4-23',
        'fullfilment_status': 'Completed',
        'warehouse_id':'02'
    },
]
# For ptoduct----------------------------------------------------------------

def addProducts(product_name,sku,category,sub_category,image_link):
    #condition for sku if already exist
    for product in product_catalog:
        if product['sku'] == sku:
            print(f"Sku {sku} is already exist please try another!")
            return

    #adding product
    product={
        'name':product_name,
        'sku':sku,
        'category': category,
        'sub_category':sub_category,
        'image_link':image_link
    }

    product_catalog.append(product)
    print(f"Product {product_name} name added successfully!!")

# For Warehouse-----------------------------------------------------------

def addWarehouse(warehouse_id, name, state, location, stock_limit=None):
    for warehouse in warehouse_catalog:
        if warehouse['warehouse_id'] == warehouse_id:
            print(f"Warehouse id {warehouse_id} is already exist please try another!")
            return

    #adding warehouse
    new_warehouse={
        'warehouse_id':warehouse_id,
        'name':name,
        'state': state,
        'location':location,
        'stock_limit':stock_limit
    }

    warehouse_catalog.append(new_warehouse)
    print(f"Warehouse id {warehouse_id}  added successfully!!")

#Command-3  ADD STOCK----------------------------

def addStock(sku, warehouse_id, quantity):
    product=None
    warehouse=None

    # in product_catalog to find the product of given sku
    for p in product_catalog:
        if p['sku']==sku:
            product=p
            break
    # in warehouse_catalog to find the warehouse  of given id
    for w in warehouse_catalog:
        if w['warehouse_id']==warehouse_id:
            warehouse=w
            break

    if product is None:
        print(f"Product with SKU {sku} not exist")
        return
    if warehouse is None:
        print(f"Warehouse with ID {warehouse_id} not exist")
        return

    # Checking the warehouse is having stock limit
    stock_limit=warehouse['stock_limit']
    if stock_limit is not None:
        current_stock = warehouse.get('stock',0)
        available_stock = stock_limit - current_stock

        if quantity > available_stock:
            print(f"Warning: the quaantitdy is exceeded then warehouse{warehouse_id} stock."
                    f"Only {available_stock} is available.")

    #Adding stock to the warehouse
    warehouse.setdefault('stock',0)
    warehouse['stock'] += quantity
    print(f"Stock added: {quantity} item(s) of {product['name']} (Sku:{sku}) added to Warehouse {warehouse_id}")


# Command -4 ADD STATE

state_catalog=['AP','Kerala','KA','TN']
def addState(state):
    if state in state_catalog:
        print(f"State {state} already exists")
    else:
        state_catalog.append(state)
        print(f"State {state} added Successfully")


# Command-5 VIEW STATE

def viewState():
    state_info=[]
    for state in state_catalog:
        warehouse_count =sum(1 for warehouse in warehouse_catalog if warehouse['state']==state)
        stock_capacity =sum(warehouse.get('stock_limit',0) for warehouse in warehouse_catalog if warehouse['state']==state)
        state_info.append({'state': state, 'warehouse_count':warehouse_count, 'stock_capacity':stock_capacity})

    headers=['State', 'Warehouse Count','Total Stock Capacity']
    rows=[ [state['state'],state['warehouse_count'],state['stock_capacity']] for state in state_info]
    print(tabulate(rows, headers, tablefmt='grid'))


# Command-6===Command 3
# Command-7 PROCESS ORDER
def processOrder(customer_id, sku, order_qty, customer_location):
    customer=None
    for c in customer_database:
        if c['customer_id']==customer_id:
            customer=c
            break

        if customer is None:
            print(f"Customer with ID {customer_id} not found in customer DB")
            return
        #calculating distance customer location to warehouse
        warehouse_distance=[]
        for w in warehouse_catalog:
            distance=calculateDistance(customer_location, w['location'])
            warehouse_distance.append({'warehouse':w, 'distance':distance })

        #sorting warehouse based on distance in asecnfing order
        warehouse_distance.sort(key=lambda x:x['distance'])

        for warehouse_distance in warehouse_distance:
            w=warehouse_distance['warehouse']
            stock=w.get('stock',0)
            if stock >=order_qty:
                w['stock'] -= order_qty
                print(f"Order passed for CustomerID{customer_id} is Successfull."
                    f"SKU:{sku}, Quantity: {order_qty}, Warehouse ID:{w['warehouse_id']}")
                return
        print(f"Order cannot be fullfilled for Customer ID: {customer_id}, SKU: {sku}, Quantity: {order_qty}")

def calculateDistance(loc1,loc2):
    lat1, lon1=loc1
    lat2, lon2= loc2

    #calcuating distance using formula haversine(θ) = sin²(θ/2) [haversine]-reference[https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula]
    dlat=math.radians(lat2-lat1)
    dlon= math.radians(lon2 - lon1 )
    a=math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))* math.sin(dlon/2)* math.sin(dlon/2)
    c= 2* math.atan2(math.sqrt(a), math.sqrt(1-a))
    radius=6371 #radius of earth
    distance=radius*c
    return distance


# COmmand -8 VIEW ORDER
def viewOrder():
    
    headers=['order_id', 'customer_id','order_date','fullfilment_status','warehouse_id']
    rows=[ [order['order_id'],order['customer_id'],order['order_date'],order['fullfilment_status'],order['warehouse_id']] for order in order_database]
    print(tabulate(rows, headers, tablefmt='grid'))

# Command-9 LIST PRODUCTS
def listProducts():
    product_info=[]
    for p in product_catalog:
        stock_quantity=sum(warehouse.get('stock',0) for warehouse in warehouse_catalog if warehouse['warehouse_id'] in p.get('in_stock_warehouse',[]))
        product_info.append({'sku':p['sku'], 'name':p['name'], 'stock_quantity':stock_quantity, 'in_stock_warehouse':p.get('in_stock_warehouse',[])})
    
    headers=['Sku', 'Name','Stock Quantity','In Stock Warehouse']
    rows=[ [p['sku'],p['name'],p['stock_quantity'],p['in_stock_warehouse']] for p in product_info]
    print(tabulate(rows, headers, tablefmt='grid'))

#Command-10 LIST WAREHOUSE ----------------------------------
def listWarehouse():
    headers=['Warehouse ID', 'State','Location']
    rows=[ [warehouse['warehouse_id'],warehouse['state'],warehouse['location']] for warehouse in warehouse_catalog]
    print(tabulate(rows, headers, tablefmt='grid'))

#COmmand -11 WarehouseInfo
def warehouseInfo(warehouse_id):
    warehouse=None
    for w in warehouse_catalog:
        if int(w["warehouse_id"]) ==int (warehouse_id):
            warehouse=w
            break
    if warehouse is None:
        print(f"Warehouse with ID {warehouse_id} is not found")
        return
    warehouse_sku_info=[]
    for p in product_catalog:
        sku = p['sku']
        stock=warehouse.get('stock',{}).get(sku,0)
        warehouse_sku_info.append({'Sku':sku, 'Stock':stock})

    headers=['SKU','Stock']
    rows=[[info['SKU'],info['Stock']] for info in warehouse_sku_info]
    print(f"Warehouse ID: {warehouse['warehouse_id']}")
    print(f" Available Storage:{'Unlimited' if warehouse.get('stock_limit')==-1 else warehouse.get('stock_limit')}")
    print(tabulate(rows, headers, tablefmt='grid'))
