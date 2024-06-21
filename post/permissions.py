from rest_framework import permissions

class UserPermissions(permissions.BasePermission):
	edit_method = ('PUT','PATCH')



	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		if request.method in self.edit_method and request.user == obj.user :
			return True
		return False

