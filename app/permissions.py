from rest_framework import permissions


class GlobalPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permmission_codename = self.__get_model_permission_codename(request.method, view)

        if not model_permmission_codename:
            return False
        return request.user.has_perm(model_permmission_codename)

    def __get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f'{app_label}.{model_name}_{action}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        method_action = {
            'GET': 'view',
            'HEAD': 'view',
            'OPTIONS': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete'
        }
        return method_action.get(method, '')
