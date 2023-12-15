from django.urls import path
from storynator.views import home_view,voice_upload,landing_page_view


urlpatterns = [
    path('',landing_page_view,name='landing-page-view'),
    path('generate',home_view,name='home-view'),
    path('voice-upload',voice_upload,name='voice-upload'),
]