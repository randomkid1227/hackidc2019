from django.shortcuts import render, redirect
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
                return redirect('/CreateSession/')
            elif user.groups.filter(name='Customer').exists():
                return redirect('/CustomerDashboard')
        else:
            return render(request, 'login_page.html', {'exception': 'Wrong Username Or Password'})