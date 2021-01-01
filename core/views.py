from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes

from .models import User, JobType, PremiumJob, Subject, Order
from .serializers import UserReadSerializer, UserWriteSerializer, PremiumJobSerializer, PremiumJobWriteSerializer, OrderWriteSerializer, OrderSerializer
# Create your views here.


def jwt_response_payload_handler(token, user=None, request=None):
    user_ref = User.objects.only('id').get(id=user.id)
    return {
        'token': token,
        'user': UserReadSerializer(user, context={'request': request}).data,
    }


@authentication_classes([])
@permission_classes([])
class AddUser(APIView):
    """
    post:
    Add a New User Instance
    """
    queryset = User.objects.none()

    def post(self, request):
        print(request.data)
        serializer = UserWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PremiumJobList(APIView):
    """
    get:
    Return a list of all premium jobs
    """

    def get(self, request):
        premium_jobs = PremiumJob.objects.all()
        serializer = PremiumJobSerializer(premium_jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = PremiumJobWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer(self):
        return PremiumJobSerializer()


class OrderList(APIView):
    """
    get:
    Return a list of all premium jobs
    """

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = OrderWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer(self):
        return OrderWriteSerializer()
