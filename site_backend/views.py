from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import services
import json
from django.core.serializers.json import DjangoJSONEncoder



def index_router(request):
    # sum_transfer = services.get_sum_transfer_by_date()
    # spent_transfer = services.get_spent_transfer_by_date()
    # left_transfer = services.get_left_transfer()
    # sum_proped = services.get_sum_proped()
    # sum_bonuses = services.get_sum_bonuses()
    # sum_promo = services.get_sum_promo()
    if request.method == 'GET':
        print('test', services.get_emp_ammount_in_cities())
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
        print('post')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        print(start_date, end_date)
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


def directions_router(request):
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


def active_masters_router(request):
    if request.method == 'GET':
        print('am info', services.get_active_masters_info())
        return render(request, 'site_backend/active_masters.html', {
            'active_masters': services.get_active_masters_info()
        })
    return HttpResponse(status=405)


def active_master_wt_city(request, wt_id, city_id):
    if request.method == 'GET':
        return render(request, 'site_backend/active_masters.html', {
            'active_masters': services.get_active_masters_info(wt=wt_id, city=city_id)
        })
    return HttpResponse(status=405)


def active_master_online_wt(request, wt_id):
    if request.method == 'GET':
        return render(request, 'site_backend/active_masters.html', {
            'active_masters': services.get_active_masters_info(active=True, wt=wt_id)
        })
    return HttpResponse(status=405)


def active_master_exclusive_wt(request, wt_id):
    if request.method == 'GET':
        return render(request, 'site_backend/active_masters.html', {
            'active_masters': services.get_active_masters_info(exclusive=True, wt=wt_id)
        })
    return HttpResponse(status=405)


def active_master_vf(request):
    if request.method == 'GET':
        return render(request, 'site_backend/active_masters.html', {
            'active_masters': services.get_active_masters_info(vf=True)
        })
    return HttpResponse(status=405)


def master_card_router(request, master_id):
    if request.method == 'GET':
        #print(json.dumps(services.get_master_card_info(master_id), sort_keys=True, indent=1, cls=DjangoJSONEncoder))
        print(services.get_emp_wt(master_id))
        return render(request, 'site_backend/master_card.html', {
            'info': services.get_master_card_info(master_id),
            #'emp_wts': services.get_emp_wt(ma)
                                                                 })
    return HttpResponse(status=405)


@csrf_exempt
def registration_router(request):
    if request.method == 'GET':
        print(services.get_not_registered_masters())
        return render(request, 'site_backend/register.html',
                      {
                          'employees': services.get_not_registered_masters(),
                          'wt_list': services.get_wt_list(),
                      })
    elif request.method == 'POST':
        print('\n\nMETHOD POST', request.POST)
    return HttpResponse(status=405)

