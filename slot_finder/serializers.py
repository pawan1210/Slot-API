from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(required=True)
    order_weight = serializers.IntegerField(required=True)

    def validate(self, data):
        if data["order_weight"] <= 0:
            raise serializers.ValidationError("Invalid weight")
        return data


class OrderListSerializer(serializers.Serializer):
    order_list = OrderSerializer(many=True)
