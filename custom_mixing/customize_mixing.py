from django.contrib.auth.models import User
from django.shortcuts import redirect

class UserLoginMixin:

    def dispatch(self, request, *args, **kwargs):
        url = request.GET.get('next')
        if User.objects.filter(username=request.user.username).exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('accounts:login')
