"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from baizak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/<int:id>',views.ViewArticles),
    path('events/<int:id>',views.ViewEvents),
    path('eco/',views.Eco,name='eco'),
    path('',views.MainPage,name='main'),
    path('eco2/',views.Eco2,name='eco2'),
    path('eco3/',views.Eco3,name='eco3'),
    path('eco4/',views.Eco4,name='eco4'),
    path('eco5/',views.Eco5,name='eco5'),
    path('eco6/',views.Eco6,name='eco6'),
]   
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
