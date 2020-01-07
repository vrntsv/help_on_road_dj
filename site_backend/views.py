from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import services


def index_router(request):
    # sum_transfer = services.get_sum_transfer_by_date()
    # spent_transfer = services.get_spent_transfer_by_date()
    # left_transfer = services.get_left_transfer()
    # sum_proped = services.get_sum_proped()
    # sum_bonuses = services.get_sum_bonuses()
    # sum_promo = services.get_sum_promo()
    if request.method == 'GET':
        print(services.get_emp_ammount_in_cities())
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
                              'exclusive_by_wt': services.get_exclusive_ammount_wt(),
                              'work_types': services.get_work_types()

                                 }
                          )
        else:
            redirect('/')
    return HttpResponse(status=405)


# Create your views here.
