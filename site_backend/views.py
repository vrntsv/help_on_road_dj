from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.urls import reverse

from . import services
from . import bot
import json
from django.core.serializers.json import DjangoJSONEncoder


def login_router(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'site_backend/login.html')
    elif request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        print(user)
        if user is not None:
            return redirect('/')
        else:
            return render(request, 'site_backend/login.html', {
                'invalid_data': True,
            })

    # No backend authenticated the credentials


def index_router(request):
    print(request.user)
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'site_backend/index.html',
                          {
                              'sum_very_first': services.get_sum_very_first(),
                              'sum_transfer': services.get_sum_transfer_by_date(),
                              'spent_transfer': services.get_spent_transfer_by_date(),
                              'sum_proped': services.get_sum_proped_by_date(),
                              'sum_promo': services.get_sum_promo_by_date(),
                              'sum_bonuses': services.get_sum_bonuses(),
                              'sum_excl_debt': services.sum_excl_debt(),
                              'left_transfers': services.get_sum_left_transfers(),
                              'work_types': services.get_work_types(),
                              'very_first_emps': services.get_employees_very_first(),
                              'cites': services.get_active_cities(),
                              'emp_ammount_in_cities': services.get_emp_ammount_in_cities(),
                              'exclusive_by_wt': services.get_emp_ammount_wt(exclusive=True),
                              'active_by_wt': services.get_emp_ammount_wt(active=True),
                           }
                          )
        elif request.method == 'POST':
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            if start_date != '' and end_date != '':
                return render(request, 'site_backend/index.html',
                              {
                                  'sum_very_first': services.get_sum_very_first(),
                                  'sum_transfer': services.get_sum_transfer_by_date(start_date, end_date),
                                  'spent_transfer': services.get_spent_transfer_by_date(start_date, end_date),
                                  'sum_proped': services.get_sum_proped_by_date(start_date, end_date),
                                  'sum_promo': services.get_sum_promo_by_date(start_date, end_date),
                                  'sum_bonuses': services.get_sum_bonuses(),
                                  'sum_excl_debt': services.sum_excl_debt(),
                                  'left_transfers': services.get_sum_left_transfers(),
                                  'very_first_emps': services.get_employees_very_first(),
                                  'cites': services.get_active_cities(),
                                  'emp_ammount_in_cities': services.get_emp_ammount_in_cities(),
                                  'exclusive_by_wt': services.get_emp_ammount_wt(exclusive=True),
                                  'active_by_wt': services.get_emp_ammount_wt(active=True),

                                     }
                              )
            else:
                redirect('/')
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def tech_router(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            print(services.get_amo_key())
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),
                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def tech_alter_key_router(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            services.alter_amo_key(request.POST.get('new_key'))
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),

                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def tech_add_city_router(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            print(request.POST)
            services.add_city(request.POST.get('new_city'))
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),
                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def tech_delete_city_router(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            services.delete_city(request.POST.get('city_id'))
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),
                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def tech_send_message_emp_router(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bot.send_message_tech(
                text=request.POST.get('text'),
                city_list=request.POST.getlist('city_id'),
                image=request.POST.get('picture'),
                to_all=True
            )
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),
                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def tech_send_message_excl_router(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bot.send_message_tech(
                text=request.POST.get('text'),
                city_list=request.POST.getlist('city_id'),
                image=request.POST.get('picture'),
                to_excl=True
            )
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),
                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def tech_send_message_excl_router(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bot.send_message_tech(
                text=request.POST.get('text'),
                city_list=request.POST.getlist('city_id'),
                image=request.POST.get('picture'),
                to_excl=True
            )
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),
                          })
        return HttpResponse(status=405)

    else:
        return redirect('/login')



def tech_send_message_clients_router(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            bot.send_message_tech(
                text=request.POST.get('text'),
                city_list=request.POST.getlist('city_id'),
                image=request.POST.get('picture'),
                to_clients=True
            )
            return render(request, 'site_backend/tech.html',
                          {
                              'amo_key': services.get_amo_key(),
                              'cities': services.get_cities(),
                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')



def directions_router(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            return render(request, 'site_backend/directions.html',
                          {
                              'work_types': services.get_work_types(),
                          })
        elif request.method == 'POST':
            print(request.POST)
            try:
                services.add_new_work_type(request.POST.get('directions_name'),
                request.POST.get('step_0'),
                request.POST.get('step_1'),
                request.POST.get('step_2'),
                request.POST.get('step_3'),
                request.POST.get('step_4'),
                request.POST.get('step_5'),
                request.POST.get('step_6'))
            except Exception:
                redirect('directions')
                return
            return render(request, 'site_backend/directions.html',
                          {
                              'work_types': services.get_work_types(),
                           })

        return HttpResponse(status=405)
    else:
        return redirect('/login')


def directions_change_router(request, wt_id):
    if request.user.is_authenticated:

        if request.method == 'POST':
            services.change_wt(wt_id, request.POST)
            return render(request, 'site_backend/directions.html',
                          {
                              'work_types': services.get_work_types(),
                          })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def active_masters_router(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            return render(request, 'site_backend/active_masters.html', {
                'active_masters': services.get_active_masters_info()
            })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def active_master_wt_city(request, wt_id, city_id):
    if request.user.is_authenticated:

        if request.method == 'GET':
            return render(request, 'site_backend/active_masters.html', {
                'active_masters': services.get_active_masters_info(wt=wt_id, city=city_id)
            })
        return HttpResponse(status=405)
    else:
        return redirect('/login')


def active_master_online_wt(request, wt_id):
    if request.user.is_authenticated:

        if request.method == 'GET':
            return render(request, 'site_backend/active_masters.html', {
                'active_masters': services.get_active_masters_info(active=True, wt=wt_id)
            })
        return HttpResponse(status=405)


def active_master_exclusive_wt(request, wt_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'site_backend/active_masters.html', {
                'active_masters': services.get_active_masters_info(exclusive=True, wt=wt_id)
            })
        return HttpResponse(status=405)


def active_master_vf(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            return render(request, 'site_backend/active_masters.html', {
                'active_masters': services.get_active_masters_info(vf=True)
            })
        return HttpResponse(status=405)


def master_card_router(request, master_id):
    if request.user.is_authenticated:

        if request.method == 'GET':
            #print(json.dumps(services.get_master_card_info(master_id), sort_keys=True, indent=1, cls=DjangoJSONEncoder))
            print(services.get_users_deals(master_id))
            return render(request, 'site_backend/master_card.html',
                          {
                              'info': services.get_master_card_info(master_id),
                          })
        return HttpResponse(status=405)


@csrf_exempt
def registration_router(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            return render(request, 'site_backend/register.html',
                          {
                              'employees': services.get_not_registered_masters(),
                              'wt_list': services.get_wt_list(),
                          })
        elif request.method == 'POST':
            if request.POST['confirm'] == 'yes':
                print(request.POST)
                services.add_emp(request.POST.get('emp_id'), request.POST.get('emp_wt'))
                return render(request, 'site_backend/register.html',
                              {
                                  'employees': services.get_not_registered_masters(),
                                  'wt_list': services.get_wt_list(),
                              })
            else:
                print(request.POST)
                services.freeze_emp(request.POST.get('emp_id'))
                return render(request, 'site_backend/register.html',
                              {
                                  'employees': services.get_not_registered_masters(),
                                  'wt_list': services.get_wt_list(),
                                  'freeze_id': request.POST.get('emp_id'),
                              })

        return HttpResponse(status=405)


@csrf_exempt
def operators_router(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            print(services.get_operators())
            return render(request, 'site_backend/operators.html',
                          {
                            'operators': services.get_operators()
                          })
        elif request.method == 'POST':
            is_created = services.create_operator(request.POST.get('name'), request.POST.get('value'))
            # если is_created=True - выводит сообщение об успехе
            # если is_created=False - выводит сообщение об ошибке
            return render(request, 'site_backend/operators.html',
                          {
                              'operators': services.get_operators(),
                              'is_created': is_created
                          }

            )


def operators_delete_router(request, operator_id):
    if request.user.is_authenticated:

        if request.method == 'POST':
            is_deleted = services.delete_operator(operator_id)
            # если is_deleted=True - выводит сообщение об успехе
            # если is_deleted=False - выводит сообщение об ошибке
            return render(request, 'site_backend/operators.html',
                          {
                              'operators': services.get_operators(),
                              'is_deleted': is_deleted
                          }
            )
        else:
            return HttpResponse(status=405)


def history_router(request):
    if request.user.is_authenticated:

        if request.method == 'GET':
            print(services.get_history())
            return render(request, 'site_backend/history.html',
                          {
                                'history': services.get_history()
                          })
        return HttpResponse(status=405)


def clients_router(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'site_backend/client.html',
                            {
                                'clients': services.get_clients()
                            })
        elif request.method == 'POST':
            print(request.POST)
            print('teststset')
            return render(request, 'site_backend/client.html',
                            {
                                'clients': services.get_clients()
                            })
        return HttpResponse(status=405)


