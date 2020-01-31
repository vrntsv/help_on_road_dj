"""help_on_road URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
import debug_toolbar

urlpatterns = [
    path('', views.index_router, name='index_url'),
    path('directions/', views.directions_router, name='directions_url'),
    path('active_masters/', views.active_masters_router, name='am_url'),
    path('active_masters?wt=<int:wt_id>;city=<int:city_id>/', views.active_master_wt_city, name='am_url_wt_city'),
    path('active_masters?wt=<int:wt_id>;active=1/', views.active_master_online_wt, name='am_url_wt_online'),
    path('active_masters?wt=<int:wt_id>;exclusive=1/', views.active_master_exclusive_wt, name='am_url_wt_exсlusive'),
    path('active_masters?vf=1', views.active_master_vf, name='am_url_vf'),
    path('master_card?id=<int:master_id>', views.master_card_router, name='master_card_url'),

]
