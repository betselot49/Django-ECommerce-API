from rest_framework import permissions
# Only authenticated users can create, update, delete, and view orders
# Only staff users can view all orders

class IsOwnerOrStaffOrNone(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user.profile == obj.user:
            return True
        
        if request.user.is_staff and request.user.profile != obj.user:
            return request.method == 'GET' or request.method == 'DELETE'
    
        return False
        
class IsAllowedToViewOrderItems(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated or request.user.is_staff
    
    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.order.user