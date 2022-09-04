from rest_framework import permissions


class IsMember(permissions.BasePermission):
    """
    Allows access only to library member.
    """
    def has_permission(self, request, view):
        if request.user:
            if not request.user.is_staff:
                return True


class IsLibrarian(permissions.BasePermission):
    """
    Allows access only to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsLibrarianOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id