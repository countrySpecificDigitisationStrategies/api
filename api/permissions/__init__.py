from rest_framework.permissions import BasePermission


class UserIsUserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class UserIsObjectOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user

class UserIsObjectOwnerOrModeratorPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_moderator
