from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'/(?P<company>[\w|-|_|\s|.]+)/AcceptSession', CompanySessionAccept.as_view()),
    url(r'/(?P<company>[\w|-|_|\s|.]+)/DeclineSession', CompanySessionDecline.as_view()),
    url(r'/(?P<company>[\w|-|_|\s|.]+)/RequestCall', CompanySessionRequestCall.as_view()),
    url(r'/(?P<company>[\w|-|_|\s|.]+)/', CompanySession.as_view()),
]
