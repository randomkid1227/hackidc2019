"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
    url(r'^admin/', admin.site.urls),
    url(r'^login', include('login.urls')),
    url(r'^logo.png', include('login.urls')),
    url(r'^CustomerDashboard', include('customer_dashboard.urls')),
    url(r'^CompanySessionConfirmed', include('company_session_confirmed.urls')),
    url(r'^CompanySession', include('company_session.urls')),
    url(r'^CreateSession', include('company_create_session.urls')),
    url(r'^ViewSessions', include('view_sessions.urls')),
    url(r'^ViewRequests', include('view_requests.urls')),
    url(r'^$', include('login.urls'))

]
