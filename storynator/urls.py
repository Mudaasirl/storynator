from django.urls import path
from storynator.views import home_view,voice_upload,landing_page_view
from . import views
from storynator.views import AuthGoogle


urlpatterns = [
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', AuthGoogle.as_view(), name='auth_receiver'),
    path('',landing_page_view,name='landing-page-view'),
    path('generate',home_view,name='home-view'),
    path('voice-upload',voice_upload,name='voice-upload'),
]