from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection
from .companies_description import *


class CompanySessionAccept(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'on_click.html', {
            'session_id': get_active_session(company, request.user.username),
            'company':company,
            'description': description[company],
            'url':urls[company]
        })

    def post(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        username = request.user.username
        key_id = request.POST.get("key_id", "-1")
        cursor = connection.cursor()
        cursor.callproc("customer_key_action", [company, username, key_id, "approved"])
        response = cursor.fetchall()
        print(response)
        cursor.close()

        return render(request, 'on_click.html', {
            'session_id': get_active_session(company, request.user.username),
            'company': company,
            'description': description[company],
            'url': urls[company],
            'session_accepted': True
        })


class CompanySessionDecline(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'on_click.html', {'session_id': get_active_session(company, request.user.username), 'company':company, 'description': description[company],
            'url':urls[company]})

    def post(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        username = request.user.username
        key_id = request.POST.get("key_id", "-1")
        cursor = connection.cursor()
        cursor.callproc("customer_key_action", [company, username, key_id, "declined"])
        response = cursor.fetchall()
        cursor.close()

        return render(request, 'on_click.html',
                      {'session_id': get_active_session(company, request.user.username), 'company': company,
                       'description': description[company],
                       'url': urls[company], 'session_rejected': True})


class CompanySessionRequestCall(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'on_click.html', {'session_id': get_active_session(company, request.user.username), 'company':company, 'description': description[company],
            'url':urls[company]})

    def post(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        cursor = connection.cursor()
        cursor.callproc("add_call_request", [request.user.username, company])
        response = cursor.fetchall()
        cursor.close()

        return render(request, 'on_click.html',
                      {'call_request_added':True, 'company': company,'session_id': get_active_session(company, request.user.username), 'call_request':True})


class CompanySession(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        return render(request, 'on_click.html',
                      {'session_id': get_active_session(company, request.user.username), 'company': company, 'description': description[company],
            'url':urls[company]})


def get_active_session(company, username):
    try:
        cur = connection.cursor()
        cur.callproc('get_active_session', [company, username])
        result = cur.fetchall()
        if result:
            return result[0][0]
        return None
    except:
        return None
    finally:
        cur.close()
