# your_project/middleware.py

# function based middlewares
# def mymiddlewale(get_response):
#     def middleware(request):
#         return get_response(request)
#     return middleware


# class based middleware
class simplemiddleware:
    #initail configuration
    def __init__(self,get_response):
        self.get_response=get_response
    
    def __call__(self,request):
        #code executed before view
        print("executed before view")
        response=self.get_response(request)
        #code exected after view is called
        print("executed after view")
        return response

from django.http import HttpResponseRedirect
from django.urls import reverse

class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is trying to access the admin page
        if request.path.startswith('/admin/'):
            if request.user.is_authenticated:
                # Replace 'your_admin_username' with the username of the allowed admin
                if request.user.username != 'admin':
                    return HttpResponseRedirect(reverse('policy_list'))  # Redirect to home page or another page

        response = self.get_response(request)
        return response
