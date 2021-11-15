from rest_framework.permissions import IsAuthenticated

from account.models import User
from .permission import ViewAndEditOwnProfile
from .serializers import UserSerializer, AddExpense, CreateCategory, CreateMonth
from rest_framework import generics


# api for tha account app

class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, ViewAndEditOwnProfile)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(generics.GenericAPIView):
    pass

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Api for the expense app
class AddExpenses(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AddExpense

    def perform_create(self, serializer):
        serializer.save()


class CreateCategory(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateCategory

    def perform_create(self, serializer):
        serializer.save()


class CreateMonth(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateMonth

    def perform_create(self, serializer):
        serializer.save()
