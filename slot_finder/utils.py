import copy

from .constants import vehicle_capacity, max_optimal_space_wasted, slots


class SlotFinder:
    def __init__(self):
        self.vehicles = []
        self.optimal_space_wasted = max_optimal_space_wasted
        self.optimal_vehicle_distribution = []

    def assign_orders(self, order_list, vehicles, index):
        if index == len(order_list):
            space_wasted = 0
            for vehicle in vehicles:
                if vehicle["current_capacity"] > 0:
                    space_wasted += vehicle["capacity"] - vehicle["current_capacity"]

            if space_wasted < self.optimal_space_wasted:
                self.optimal_space_wasted = space_wasted
                self.optimal_vehicle_distribution = copy.deepcopy(vehicles)

            return

        for i in range(0, len(vehicles)):
            if (
                vehicles[i]["current_capacity"] + order_list[index]["order_weight"]
                <= vehicles[i]["capacity"]
            ):
                vehicles[i]["current_capacity"] += order_list[index]["order_weight"]
                vehicles[i]["orders_list"].append(order_list[index]["order_id"])
                self.assign_orders(order_list, vehicles, index + 1)
                vehicles[i]["current_capacity"] -= order_list[index]["order_weight"]
                vehicles[i]["orders_list"].pop()

    def find_slot(self, order_list):
        for capacity in vehicle_capacity:
            self.vehicles.append(
                {"capacity": capacity, "orders_list": [], "current_capacity": 0}
            )

        self.assign_orders(order_list, self.vehicles, 0)
        self.divide_in_slots()

    def divide_in_slots(self):
        filled_slots = dict(slots)
        for vehicle in self.optimal_vehicle_distribution:
            if (
                (vehicle["capacity"] == 30 or vehicle["capacity"] == 50)
                and vehicle["current_capacity"] > 0
                and filled_slots["6-9"]["total_weight"] + vehicle["current_capacity"]
                <= 100
            ):
                filled_slots["6-9"]["shipments"].append(vehicle)
                filled_slots["6-9"]["total_weight"] += vehicle["current_capacity"]
                self.optimal_vehicle_distribution.remove(vehicle)

        for vehicle in self.optimal_vehicle_distribution:
            if (
                filled_slots["9-13"]["total_weight"] + vehicle["current_capacity"]
                <= 100
                and vehicle["current_capacity"] > 0
            ):
                filled_slots["9-13"]["shipments"].append(vehicle)
                filled_slots["9-13"]["total_weight"] += vehicle["current_capacity"]
                self.optimal_vehicle_distribution.remove(vehicle)

        for vehicle in self.optimal_vehicle_distribution:
            if (
                filled_slots["16-19"]["total_weight"] + vehicle["current_capacity"]
                <= 100
                and vehicle["current_capacity"] > 0
            ):
                filled_slots["16-19"]["shipments"].append(vehicle)
                filled_slots["16-19"]["total_weight"] += vehicle["current_capacity"]
                self.optimal_vehicle_distribution.remove(vehicle)

        for vehicle in self.optimal_vehicle_distribution:
            if (
                (vehicle["capacity"] == 100)
                and vehicle["current_capacity"] > 0
                and filled_slots["19-23"]["total_weight"] + vehicle["current_capacity"]
                <= 100
            ):
                filled_slots["19-23"]["shipments"].append(vehicle)
                filled_slots["19-23"]["total_weight"] += vehicle["current_capacity"]
                self.optimal_vehicle_distribution.remove(vehicle)

        print(filled_slots)
