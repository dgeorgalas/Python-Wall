from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wall$', views.wall),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^log_out', views.log_out),
    url(r'^message/delete/(?P<message_id>\d+)$', views.delete_message),
]