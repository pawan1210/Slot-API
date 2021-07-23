delivery_partners = [
    {"id": "1", "vehicle_capacity": 30, "vehicle_type": "bike"},
    {"id": "2", "vehicle_capacity": 30, "vehicle_type": "bike"},
    {"id": "3", "vehicle_capacity": 30, "vehicle_type": "bike"},
    {"id": "4", "vehicle_capacity": 50, "vehicle_type": "scooter"},
    {"id": "5", "vehicle_capacity": 50, "vehicle_type": "scooter"},
    {"id": "6", "vehicle_capacity": 100, "vehicle_type": "truck"},
]
max_optimal_space_wasted = 290
slots = {
    "6-9": {"shipments": [], "total_weight": 0},
    "9-13": {"shipments": [], "total_weight": 0},
    "16-19": {"shipments": [], "total_weight": 0},
    "19-23": {"shipments": [], "total_weight": 0},
}

error_response = {"message": "Invalid input"}

