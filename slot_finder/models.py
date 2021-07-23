from django.db import models


class Vehicle(models.Model):
    vehicle_type_choices = [
        ("bike", "bike"),
        ("scooter", "scooter"),
        ("truck", "truck"),
    ]

    vehicle_type = models.CharField(
        max_length=100, choices=vehicle_type_choices, blank=False,
    )
    capacity = models.IntegerField()

    def __str__(self):
        return self.vehicle_type


class DelieveryPartner(models.Model):
    vehicle = models.ForeignKey("Vehicle", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, unique=True, blank=False)

    def __str__(self):
        return self.delievery_partner_id


class Shipment(models.Model):
    slot_id_choices = [(1, "6-9"), (2, "9-13"), (3, "16-19"), (4, "19-23")]

    slot_id = models.IntegerField(blank=False, choices=slot_id_choices)
    date = models.DateField(auto_now_add=True)
    delievery_partner_id = models.ForeignKey(
        "DelieveryPartner", on_delete=models.SET_NULL, null=True
    )
    order_id = models.IntegerField(blank=False)

    def __str(self):
        return delievery_partner_id + " " + order_id

