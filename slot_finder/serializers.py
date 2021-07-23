from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(required=True)
    order_weight = serializers.IntegerField(required=True)


class OrderListSerializer(serializers.Serializer):
    order_list = OrderSerializer(many=True)
