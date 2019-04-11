from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection


class SessionConfirmed(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        return render(request, 'company_session_confirmed.html', {'company':company})

