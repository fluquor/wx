from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.WeChat.as_view(),name='index')
]