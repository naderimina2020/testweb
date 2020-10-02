from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('about/', views.about,name='about'),
    path('', views.home,name='home'),
    path('password/', views.password,name='password'),
    path('articles/',include('articles.urls')),
    # path('kala/',include('kala.urls')),
    path('accounts/',include('accounts.urls')),
    # path('home/',include('home.urls')),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns+=staticfiles_urlpatterns()
