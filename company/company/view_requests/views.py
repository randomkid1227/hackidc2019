from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection


class ViewRequests(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'view_requests.html', {'requests': view_company_requests(request.user.username)})


def view_company_requests(company):
    try:
        cur = connection.cursor()
        cur.callproc('get_company_requests', [company])
        result = cur.fetchall()
        return result
    except:
        return None
    finally:
        cur.close()
