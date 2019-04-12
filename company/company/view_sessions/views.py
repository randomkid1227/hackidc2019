from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection


class ViewSessions(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'view_sessions.html' , {'sessions': view_company_sessions(request.user.username)})


def view_company_sessions(company):
    try:
        cur = connection.cursor()
        cur.callproc('view_company_sessions', [company])
        result = cur.fetchall()
        return result
    except:
        return None
    finally:
        cur.close()
