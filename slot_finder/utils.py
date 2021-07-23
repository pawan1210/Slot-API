import copy

from .constants import (
    delivery_partners,
    max_optimal_space_wasted,
    slots,
    error_response,
)


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
                    space_wasted += (
                        vehicle["vehicle_capacity"] - vehicle["current_capacity"]
                    )

            if space_wasted < self.optimal_space_wasted:
                self.optimal_space_wasted = space_wasted
                self.optimal_vehicle_distribution = copy.deepcopy(vehicles)

            return

        for i in range(0, len(vehicles)):
            if (
                vehicles[i]["current_capacity"] + order_list[index]["order_weight"]
                <= vehicles[i]["vehicle_capacity"]
            ):
                vehicles[i]["current_capacity"] += order_list[index]["order_weight"]
                vehicles[i]["list_orders_ids_assigned"].append(
                    order_list[index]["order_id"]
                )
                self.assign_orders(order_list, vehicles, index + 1)
                vehicles[i]["current_capacity"] -= order_list[index]["order_weight"]
                vehicles[i]["list_orders_ids_assigned"].pop()

    def find_slot(self, order_list):
        for delivery_partner in delivery_partners:
            self.vehicles.append(
                {
                    "vehicle_capacity": delivery_partner["vehicle_capacity"],
                    "list_orders_ids_assigned": [],
                    "current_capacity": 0,
                    "vehicle_type": delivery_partner["vehicle_type"],
                    "delivery_partner_id": delivery_partner["id"],
                }
            )

        self.assign_orders(order_list, self.vehicles, 0)
        filled_slots = self.divide_in_slots()

        return (
            filled_slots
            if self.validate_orders(order_list, filled_slots)
            else error_response
        )

    def divide_in_slots(self):
        filled_slots = copy.deepcopy(slots)
        for key in slots:
            for vehicle in self.optimal_vehicle_distribution:
                if self.validate_slot(slots, key, vehicle):
                    filled_slots[key]["shipments"].append(vehicle)
                    filled_slots[key]["total_weight"] += vehicle["current_capacity"]
                    self.optimal_vehicle_distribution.remove(vehicle)
        return filled_slots

    def validate_slot(self, slots, key, vehicle):
        if vehicle["current_capacity"] == 0:
            return False
        if slots[key]["total_weight"] + vehicle["current_capacity"] > 100:
            return False
        if key == "6-9" and (vehicle["vehicle_capacity"] == 100):
            return False
        if key == "19-23" and (
            vehicle["vehicle_capacity"] == 30 or vehicle["vehicle_capacity"] == 50
        ):
            return False
        return True

    def validate_orders(self, order_list, filled_slots):
        total_orders_weight = 0
        total_slots_weight = 0
        for order in order_list:
            total_orders_weight += order["order_weight"]
        for slot in filled_slots:
            total_slots_weight += filled_slots[slot]["total_weight"]
        return total_orders_weight == total_slots_weight

