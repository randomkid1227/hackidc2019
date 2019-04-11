from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection


class CompanySessionAccept(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'on_click.html', {'session_id': get_active_session(company, request.user.username), 'company':company})

    def post(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        username = request.user.username
        key_id = request.post.get("key_id", "-1")
        cursor = connection.cursor()
        cursor.callproc("customer_key_action", [company, username, key_id, "approved"])
        response = cursor.fetchall()
        cursor.close()


class CompanySessionDecline(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'on_click.html', {'session_id': get_active_session(company, request.user.username), 'company':company})

    def post(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        username = request.user.username
        key_id = request.post.get("key_id", "-1")
        cursor = connection.cursor()
        cursor.callproc("customer_key_action", [company, username, key_id, "declined"])
        response = cursor.fetchall()
        cursor.close()


class CompanySessionRequestCall(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'on_click.html', {'session_id': get_active_session(company, request.user.username), 'company':company})

    def post(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')


class CompanySession(View):
    def get(self, request, company):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        return render(request, 'on_click.html',
                      {'session_id': get_active_session(company, request.user.username), 'company': company})


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
