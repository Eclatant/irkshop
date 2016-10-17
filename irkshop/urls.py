from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings

from goods import views as goods_views


urlpatterns = [
    url(r'^accounts/login/$', login,
        {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', admin.site.urls),
    url(r'^$', goods_views.index),
]
