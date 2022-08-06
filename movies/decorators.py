from django.http import HttpResponse
from .models import UserInfo

def student_only(func):
	def wrapper(request, *args, **kwargs):
		if UserInfo.objects.filter(pk = request.user.id, user_type = "Student").exists():
			return func(request, *args, **kwargs)
		else:
			return HttpResponse("You have no permission to upload videos, Please sign up as Student!")
	return wrapper