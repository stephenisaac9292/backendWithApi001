from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Seller').exists()

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Customer').exists()

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Staff').exists()
