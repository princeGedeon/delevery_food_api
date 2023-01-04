from rest_framework import permissions

class IsHighUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user:
            return (request.user.profile == 'ADMIN' or request.user.profile== 'SUPERADMIN' or request.user.profile=="GERANT")
        else:
            return False
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.profile == 'ADMIN' or request.user.profile== 'SUPERADMIN')
