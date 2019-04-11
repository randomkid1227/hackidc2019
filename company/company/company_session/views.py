from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection


class CompanySession(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'company_session.html', {'session': get_active_session(company, request.user.username)})

    def post(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')


def get_active_session(company, username):
    try:
        cur = connection.cursor()
        cur.callproc('get_active_session', [company, username])
        result = cur.fetchall()
        if result:
            return result[0]
        return None
    except:
        return None
    finally:
        cur.close()
