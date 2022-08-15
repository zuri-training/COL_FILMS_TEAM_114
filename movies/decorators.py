# from django.http import HttpResponse
# from .models import UserInfo

# def student_only(func):
# 	def wrapper(request, *args, **kwargs):
# 		if UserInfo.objects.filter(pk = request.user.id, user_type = "Student").exists():
# 			return func(request, *args, **kwargs)
# 		else:
# 			return HttpResponse("You have no permission to upload videos, Please sign up as Student!")
# 	return wrapper


from functools import wraps
from django.http import HttpResponse

def student_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        profile = request.user.userinfo
        if profile.user_type == 'Student':
             return function(request, *args, **kwargs)
        else:
            return HttpResponse('You have no permission to upload videos, Please sign up as Student!')
  return wrap