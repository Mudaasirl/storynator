from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.conf import settings
from storynator.views import sign_out,AuthGoogle
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog_views.home,name='home'),
    path('blog/', include("blog.urls")),
    path('storynator/',include("storynator.urls")),    
    path('sign-out', sign_out, name='sign_out'),
    path('auth-receiver', AuthGoogle.as_view(), name='auth_receiver'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)