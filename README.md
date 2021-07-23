# SLOT API
A Rest API which first assigns orders to vehicles optimally and then divide them into slots.

## 🚧 Technology Stack

- **Framework** - Django Rest Framework ( GenericAPIView is used)
- **Python** - version 3.8.3


## ⬇️ Installation on local host

```
# clone the repository to your local machine
$ git clone https://github.com/pawan1210/Slot-API.git

# navigate to the project's directory and install all the relevant dev-dependencies
$ cd slot_api

# Create a .env file 
SECRET_KEY = <key>
DEBUG = <True or False>

# Create Virtual Environment
$ python -m venv ./venv

# Activate Virtual Environment
$ For Mac -  source ./venv/bin/activate
$ For Windows -  . venv/Scripts/activate

# install dependencies
$ pip install -r requirements.txt 

# Start application
$ python manage.py runserver

# Visit http://127.0.0.1:8000/ in your browser
```

# Algorithm for vehicle distribution.
A Recursive algorithm is used to find the most optimal distribution that minimizes the wasteage of space in vehicles.

```
def assign_orders (order_list,vehicles,index):
    check if index==len(order_list):
        - find space_wasted in current distribution
        - if space+wasted is less than current optimal then assign this distribution   as optimal distribution.
        - return
    for i in range(0,len(vehicles):
        check if vehicle[i][capacity] + order[index][weight]<=100
         - add this order in the vehicle
         - recursively call for next iteration
         - assign_orders(order_list,vehivles,index+1)
         - remove this order from vehicle
    return
```
    
In the end we would have the most optimal distribution of orders that minimizes wastage of space in vehicles.
    
# Structure for a vehicle
```
{
    "vehicle_capacity": 30,
    "list_orders_ids_assigned": [],
    "current_capacity": 0,
    "vehicle_type": "bike",
    "delivery_partner_id": 1,
}
```

## 🔨 API Endpoints
###### [VIEW POSTMAN DOCUMENTATION](https://www.getpostman.com/collections/a9b630ed823e04eb158a)

| REQUEST METHODS |      ENDPOINTS      |                                       |
| :-------------- | :-----------------: | ------------------------------------------------: |
| POST            |    /find_slot    |     

## Request Body
```
{
    "order_list":[
        {
            "order_id":1,
            "order_weight":10
        }
    ]
}
```
## Output Response
### - (a) If input request is valid
```
{
    "6-9": {
        "shipments": [],
        "total_weight": 0
    },
    "9-13": {
        "shipments": [],
        "total_weight": 0
    },
    "16-19": {
        "shipments": [],
        "total_weight": 0
    },
    "19-23": {
        "shipments": [],
        "total_weight": 0
    }
}

** Shipment would contain vehicles as described above
```

### - (b) If input request is valid but orders are not deliverable based on given         constraints
```
{
    "message":"Invalid Data"
}
```
### - (c ) If input request is invalid
```
 Errors based on request serializer.
```

# Database Models
- Proper field choices are used.
- Blank and null checks are done properly.
- Proper referencing is done.
```
Vehicle
    vehicle_type_choices = [
        ("bike", "bike"),
        ("scooter", "scooter"),
        ("truck", "truck"),
    ]

    vehicle_type = string
    capacity = int



DelieveryPartner
    vehicle = foreign key
    name = string
    
Shipment
    slot_id_choices = [(1, "6-9"), (2, "9-13"), (3, "16-19"), (4, "19-23")]

    slot_id = int
    date = date
    delievery_partner_id = foreign key 
    order_id = models.IntegerField(blank=False)
```

## Explanation
 - Hierarchy- Vehicle - > Delivery Partner - > Shipment
 - Vehicle describes the available vehicles for all partners.
 - Vehicle is referenced in Delivery Partner as a foreign key.
 - Delivery partner is referenced in Shipment along with order_id and slot_id.
 - Slot_id defines the slot timings.

## Rules/Assumptions
1. Order list is for whole day.
2. Optimization is done on the basis of vehicle capacity



