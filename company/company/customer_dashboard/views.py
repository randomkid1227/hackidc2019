from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect


class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, 'customer_dashboard.html')
        else:
            return redirect('/Login/')

