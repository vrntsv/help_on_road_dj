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
    path('login', views.login_router, name='login_url'),
    path('logout', views.logout_router, name='logout_url'),
    path('directions/', views.directions_router, name='directions_url'),
    path('directions?change=<int:wt_id>', views.directions_change_router, name='directions_change_url'),
    path('active_masters/', views.active_masters_router, name='am_url'),
    path('active_masters/search', views.active_masters_search_router, name='am_search_url'),
    path('frozen_masters/', views.frozen_masters_router, name='frozen_url'),
    path('blocked_masters/', views.blocked_masters_router, name='blocked_url'),
    path('statistic/', views.statistic_router, name='statistic_url'),
    path('active_masters?wt=<int:wt_id>;city=<int:city_id>/', views.active_master_wt_city, name='am_url_wt_city'),
    path('active_masters?wt=<int:wt_id>;active=1/', views.active_master_online_wt, name='am_url_wt_online'),
    path('active_masters?wt=<int:wt_id>;exclusive=1/', views.active_master_exclusive_wt, name='am_url_wt_exсlusive'),
    path('active_masters?vf=1', views.active_master_vf, name='am_url_vf'),
    path('active_masters/exclusive=True?negative_balance=True', views.active_masters_excl_negative_balance, name='am_excl_nb'),
    path('active_masters/positive_balance=True', views.active_masters_positive_balance, name='am_pb'),
    path('active_masters/reg_today=True', views.active_masters_reg_today, name='am_reg_today'),
    path('active_masters/edit=<int:master_id>', views.edit_users_data_router, name='edit_users_data'),
    path('master_card?id=<int:master_id>', views.master_card_router, name='master_card_url'),
    path('master_card?id=<int:master_id>?write_off', views.master_card_write_off_router, name='master_card_write_off_url'),
    path('master_card?id=<int:master_id>?charge', views.master_card_charge_router, name='master_card_charge_url'),
    path('registration', views.registration_router, name='registration_url'),
    path('operators', views.operators_router, name='operators_url'),
    path('operators?delete=<int:operator_id>', views.operators_delete_router, name='operators_delete_url'),
    path('history', views.history_router, name='history_url'),
    path('сlients', views.clients_router, name='clients_url'),
    path('tech', views.tech_router, name='tech_url'),
    path('tech/alter_key', views.tech_alter_key_router, name='tech_alter_key_url'),
    path('tech/add_city', views.tech_add_city_router, name='tech_add_city_url'),
    path('tech/delete_city', views.tech_delete_city_router, name='tech_delete_city_url'),
    path('tech/send_message_emp', views.tech_send_message_emp_router, name='tech_send_message_emp_url'),
    path('tech/send_message_excl', views.tech_send_message_excl_router, name='tech_send_message_excl_url'),
    path('tech/send_message_client', views.tech_send_message_clients_router, name='tech_send_message_client_url'),

]
