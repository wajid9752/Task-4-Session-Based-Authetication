from django.shortcuts import redirect


class LoginCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path, "Request path is ")
        if request.path not in ["/login/"]:
            if "token" not in request.session:
                return redirect('login')
            else:
                if request.path in ['/login/']:
                    if "token" in request.session:
                        return redirect("dashbaord")
                 
        
        return self.get_response(request)