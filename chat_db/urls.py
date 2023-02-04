from django.conf.urls import url
from chat_db import views

urlpatterns = [
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^records/(?P<bot_id>\d+)/$', views.records_view, name='records'),
]