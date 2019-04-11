from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection


class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated():

            return render(request, 'customer_dashboard.html', {'companies': get_companies()})
        else:
            return redirect('/Login/')


def get_companies():
    try:
        cur = connection.cursor()
        cur.callproc('get_companies')
        result = cur.fetchall()
        return [company[0] for company in result]
    except:
        return None
    finally:
        cur.close()
