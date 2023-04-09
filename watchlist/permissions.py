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
        

class IsReviewUserOrReadOnly(permissions.BasePermission):
    """
        Allows user to update/delete reviews
        only is the user is the review user or admin user
        else only read request is permitted.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff