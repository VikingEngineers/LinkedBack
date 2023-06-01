from rest_framework import permissions
from django.contrib.auth.models import User
from lm_users.models import Profile


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to only allow administrator to edit an object.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            profile = Profile.objects.get(owner=request.user)
            return bool(obj.owner == request.user or obj.owner == profile)


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(owner=request.user)
        return bool(obj.owner == request.user or obj.owner == profile or request.user.is_staff)


class IsOwnerOrRecipientOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        profile = Profile.objects.get(owner=request.user)
        return bool(obj.sender == profile or obj.recipient == profile or request.user.is_staff)
