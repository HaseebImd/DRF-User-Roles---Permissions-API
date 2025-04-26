from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from django.contrib.auth.models import Group, Permission
from .models import User
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]  # Only logged-in users can access


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAdminUser]  # Only Admins can manage Groups


class PermissionViewSet(
    viewsets.ReadOnlyModelViewSet
):  # Only read (no create/update/delete)
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]


from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegisterSerializer


@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User created successfully",
                    "user": UserSerializer(user).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
