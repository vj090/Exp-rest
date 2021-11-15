from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()

class ViewAndEditOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.id == request.user.id
