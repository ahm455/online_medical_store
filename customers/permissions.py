from rest_framework import permissions

class CustomPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            return True

        if user.is_staff and request.method in ('POST', 'PUT', 'PATCH'):
            return True

        if user.is_superuser and request.method == 'DELETE':
            return True

        return False