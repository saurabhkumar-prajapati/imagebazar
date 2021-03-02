from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    #url(r'^about/$',views.AboutView.as_view(),name='about'),


]
