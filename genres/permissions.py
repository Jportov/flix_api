from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    """
    Custom permission class to allow only authenticated users to access genre-related views.
    """

    def has_permission(self, request, view):
        assinatura = Assinatura.objects.filter(user=request.user).first()
        if assinatura and assinatura.is_active:
            return True
        return False
