from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):

    """
    Custome permissions for UserViewSet to only allow user to edit their own profile. Otherwise GET and POST only.
    """

    # Pass for GET and POST requests
    def has_permission(self, request, view): return True


    # Only allow user to edit their own profile
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return obj == request.user

        return False
    

class IsProfileOwnerOrReadOnly(permissions.BasePermission):

    """
    Custome permissions for ProfileViewSet to only allow user to edit their own profile. Otherwise GET only.
    """

    # Pass for GET requests
    def has_permission(self, request, view): return True


    # Only allow user to edit their own profile
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return obj == request.user.profile

        return False