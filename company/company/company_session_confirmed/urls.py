from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'/(?P<company>\w+)', SessionConfirmed.as_view()),
]
