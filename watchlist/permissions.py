from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """
        Allows user to perform create/update request
        only is the user is the admin user else
        only read request is permitted.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)