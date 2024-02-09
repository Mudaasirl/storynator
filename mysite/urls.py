from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from blog import views as blog_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from views import Home # new
from storynator.views import sign_out,AuthGoogle
from django.conf.urls.static import static
urlpatterns = [
    path('',blog_views.home,name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include("blog.urls")),
    path('storynator/',include("storynator.urls")),
    path('register/', user_views.register, name ='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('accounts/', include('allauth.urls')), # new
    path('register', Home.as_view(), name='home'), # new
    path('sign-out', sign_out, name='sign_out'),
    path('auth-receiver', AuthGoogle.as_view(), name='auth_receiver'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)