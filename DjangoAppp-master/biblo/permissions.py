from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow read-only access to any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write (create, update, delete) operations only for admin users

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write (update, delete) operations only for the owner of the object
        return obj.user == request.user
