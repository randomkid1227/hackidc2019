from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'/(?P<company>\w+)/AcceptSession', CompanySessionAccept.as_view()),
    url(r'/(?P<company>\w+)/DeclineSession', CompanySessionDecline.as_view()),
    url(r'/(?P<company>\w+)/RequestCall', CompanySessionRequestCall.as_view()),
    url(r'/(?P<company>\w+)', CompanySession.as_view()),
]
