from rest_framework import generics
from rest_framework.response import Response

from .serializers import OrderListSerializer


class SlotFinderView(generics.GenericAPIView):
    serializer_class = OrderListSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        return Response({"response": "Valid"})
