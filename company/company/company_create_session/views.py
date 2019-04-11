from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.db import connection
import time, secrets, datetime


class CreateSession(View):
    def get(self, request):
        if not request.user.is_authenticated():
            return redirect('/Login/')
        return render(request, 'code_display.html', )

    def post(self, request):
        if not request.user.is_authenticated():
            return redirect('/Login/')

        TTL = 60 * 15

        try:
            phone_number = request.POST["phone_number"]

            customer = get_user_by_phone_number(phone_number)
            issuer = request.user.username
            key = secrets.token_urlsafe(16)
            key_timeout = request.POST.get("duration", TTL)
            expiration_time = datetime.datetime.utcfromtimestamp(time.time() + key_timeout)
            cursor = connection.cursor()
            cursor.callproc("add_key", [issuer, customer, key, expiration_time])
            response = cursor.fetchall()
            cursor.close()

            return render(request, 'code_display.html', {"ttl": expiration_time})
        except Exception as e:
            return render(request, 'code_display.html', {"errorMessage": e} )


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
