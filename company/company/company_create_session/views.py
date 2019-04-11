from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection


class CreateSession(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'create_session.html', )

    def post(self, request):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        phone_number = request.POST["phone_number"]

        username = get_user_by_phone_number(phone_number)



def get_user_by_phone_number(phone_number):
    try:
        cur = connection.cursor()
        cur.callproc('get_user_by_phone_number', [phone_number])
        result = cur.fetchall()
        if result:
            return result[0]
        return None
    except:
        return None
    finally:
        cur.close()
