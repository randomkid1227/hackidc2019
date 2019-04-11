from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout, authenticate


class Login(View):
    def get(self, request):
        return render(request, 'login_page.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.groups.filter(name='Company').exists():
                # TODO: Redirect to company dashboard
                pass
            elif user.groups.filter(name='Customer').exists():
                # TODO: Redirect to customer dashboard
                pass
        else:
            return render(request, 'login_page.html', {'exception': 'Wrong Username Or Password'})