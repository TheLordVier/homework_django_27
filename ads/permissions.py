from rest_framework import permissions

from users.models import User


class IsOwner(permissions.BasePermission):
    """
    Клаcс-допуск (разрешение) только для владельца
    """
    message = "Updating and deleting is allowed only to the owner."

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "owner"):
            owner = obj.owner
        elif hasattr(obj, "author"):
            owner = obj.author
        else:
            return False

        if request.user == owner:
            return True


class IsStaff(permissions.BasePermission):
    """
    Клаcс-допуск (разрешение) только для персонала
    """
    message = "Updating and deleting is allowed only to the admin and moderator."

    def has_permission(self, request, view):
        if request.user.role in [User.ADMIN, User.MODERATOR]:
            return True
        return False
