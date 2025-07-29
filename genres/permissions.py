from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.has_perm('genres.view_genre')
        
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.has_perm('genres.change_genre')