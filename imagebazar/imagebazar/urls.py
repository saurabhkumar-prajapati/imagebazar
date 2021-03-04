"""imagebazar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.ShowAboutPage.as_view(),name="about"),#url(r'^$', views.ShowAboutPage.as_view(),name="about")
    path('',views.ShowHomePage.as_view(),name="home"),
    #path('',views.myhome),
    path("search/", views.Search.as_view(),name="search"),
    path("searchbar/", views.searchbar,name="searchbar"),
    path('ShowHome/', views.ShowHome.as_view(),name="ShowHome"),
    path('category/<int:cid>' ,views.ShowCategoryPage.as_view()),
    path('<int:id>/', views.story_detail, name='story_detail'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)