"""insurance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from brokers.views import display_proposal_form
from brokers.views import display_proposal_form_submission
from brokers.views import display_proposal_form_submission_txt
from clients.views import verify_client


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^proposal_forms/(?P<proposal_form_id>\d+)/?$', display_proposal_form),
    url(r'^submissions/(?P<submission_id>\d+)/?$', display_proposal_form_submission),
    url(r'^submissions/(?P<submission_id>\d+)\.txt?$', display_proposal_form_submission_txt),
    url(r'^verify_client/(?P<client_id>\d+)/?$', verify_client),
]
