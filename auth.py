import time, secrets, datetime

from abc import abstractmethod
from django.db import connection
from django.views.generic import View



class AbstractRequestHandler:
    def post(self, request):
        try:
            self._post(request)
        except Exception:
            raise

    @abstractmethod
    def _post(self, request):
        raise NotImplemented


class KeyGenerator(View, AbstractRequestHandler):
    TTL = 60*15

    def _post(self, request):
        issuer = request.user.username
        customer = request.POST["customer"]
        key = secrets.token_urlsafe(16)
        key_timeout = request.POST.get("duration", self.TTL)
        expiration_time = datetime.datetime.utcfromtimestamp(time.time() + key_timeout )
        cursor = connection.cursor()
        cursor.callproc("add_key", [issuer, customer, key, expiration_time ])
        response = cursor.fetchall()
        cursor.close()
        return response[0][0] if response else None


class AcceptKey(View, AbstractRequestHandler):
    def _post(self, request):
        username = request.user.username
        customer = request.POST["customer"]
        key_id = request.post.get("key_id", "9999")
        confirmed = request.POST['action']
        cursor = connection.cursor()
        cursor.callproc("customer_key_action", [username, customer, key_id, confirmed])
        response = cursor.fetchall()
        cursor.close()
        return response[0][0] if response else None


class RequestContact(View, AbstractRequestHandler):
    def _post(self, request):
        username = request.user.username
        customer = request.POST["customer"]
        key_id = request.post.get("key_id", "9999")
        confirmed = request.POST['action']
        cursor = connection.cursor()
        cursor.callproc("customer_key_action", [username, customer, key_id, confirmed])
        response = cursor.fetchall()
        cursor.close()
        return response[0][0] if response else None
