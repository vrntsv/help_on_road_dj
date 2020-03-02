from . import models
from django.db.models import Sum, Count
import datetime
from django.contrib.auth.models import User
from datetime import date
from datetime import timedelta

from django.db import connection




def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_sum_very_first():
    """
    Доход по "Самый первый"
    :return:
    """
    obj = models.VeryFirst.objects.aggregate(Sum('price'))
    return obj['price__sum']


def get_sum_transfer_by_date(start_date=date.today() - timedelta(days=31), end_date=date.today()):
    """
    Пулучение сумму переврдов за период времени
    :param start_date:
    :param end_date:
    :return:
    """
    # print(start_date, end_date)
    obj = models.AllTransfer.objects.filter(date__gte=start_date, date__lte=end_date).aggregate(Sum('value'))
    try:
        return obj['value__sum']
    except:
        return None


def get_spent_transfer_by_date(start_date=date.today() - timedelta(days=31), end_date=date.today()):
    """
    Пулучение сумму переврдов за период времени
    :param start_date:
    :param end_date:
    :return:
    """
    # print(start_date, end_date)
    obj = models.Deals.objects.filter(date_filing__gte=start_date, date_filing__lte=end_date).aggregate(Sum('commission'))
    try:
        return obj['commission__sum']
    except:
        return None


def alter_amo_key(key):
    obj = models.Config.objects.get(id_field=1)
    obj.amo_key = key
    obj.save()


def add_city(city_name):
    city = models.City(city=city_name)
    city.save()


def delete_city(city_id):
    city = models.City.objects.get(id=city_id)
    city.delete()


def get_cities():
    return models.City.objects.all().values()


def get_users_deals(id_user):
    return models.Deals.objects.filter(id_user_id=id_user).values()


def get_amo_key():
    return models.Config.objects.filter(id_field=1).values()


def get_sum_proped_by_date(start_date=date.today() - timedelta(days=31), end_date=date.today()):
    """
    Доход по предложенным сделкам по датам
    :param start_date:
    :param end_date:
    :return:
    """
    sum = 0
    proped_ids = models.PropedDeals.objects.values('id_deal')
    print(proped_ids)
    for id in proped_ids:
        comm = models.Deals.objects.filter(date_filing__gte=start_date,
                                           date_filing__lte=end_date,
                                           id=id['id_deal']).aggregate(Sum('commission'))
        print('comm', comm)
        if comm['commission__sum']:
            sum += int(int(comm['commission__sum'])*0.33)
    return sum


def get_sum_promo_by_date(start_date=date.today() - timedelta(days=31), end_date=date.today()):
    """
    Доход по промокодам по дате
    :param start_date:
    :param end_date:
    :return:
    """
    sum = 0
    promo_fields = models.Employees.objects.filter(promo_id__isnull=False, reg_date__gte=start_date, reg_date__lte=end_date)
    for promo in promo_fields:
        sum += 500
    return sum


def get_sum_bonuses():
    """
    Пулучение сумму бонусов
    :return:
    """
    sum_bonuses = models.Employees.objects.aggregate(Sum('bonuses'))
    return sum_bonuses['bonuses__sum']


def sum_excl_debt():
    """
    Задолжность эксклюзовов
    :return:
    """
    sum = models.Employees.objects.filter(exclusive__exact=1, balance__lt=0).aggregate(Sum('balance'))
    print('sum ecxl', sum)
    return sum['balance__sum']


def get_sum_left_transfers():
    sum = models.Employees.objects.aggregate(Sum('balance'))
    return sum['balance__sum']

def get_work_types():
    """
     Получить типы работ
    """
    directions = []
    work_types = models.WorkType.objects.filter(active=1).values()

    for wt in work_types:
        directions.append(
            {
                'id': wt['id'],
                'type': wt['type'],
                'comm_stage_0': wt['comm_stage_0'],
                'comm_stage_1': wt['comm_stage_1'],
                'comm_stage_2': wt['comm_stage_2'],
                'comm_stage_3': wt['comm_stage_3'],
                'comm_stage_4': wt['comm_stage_4'],
                'comm_stage_5': wt['comm_stage_5'],
                'comm_stage_6': wt['comm_stage_6'],
                'excl_type': wt['excl_type'],
                'post_pay': wt['post_pay']
            })
    print(directions)
    return directions


def change_wt(wt_id, wt_data):
    print('tqtwet', wt_data)
    wt = models.WorkType.objects.get(id=wt_id)
    wt.type = wt_data['type']
    wt.comm_stage_0 = wt_data['step0']
    wt.comm_stage_1 = wt_data['step1']
    wt.comm_stage_2 = wt_data['step2']
    wt.comm_stage_3 = wt_data['step3']
    wt.comm_stage_4 = wt_data['step4']
    wt.comm_stage_5 = wt_data['step5']
    wt.comm_stage_6 = wt_data['step6']

    if 'post_pay' in wt_data.keys():
        wt.post_pay = 1
    else:
        wt.post_pay = None

    if 'excl_type' in wt_data.keys():
        wt.excl_type = 1
    else:
        wt.excl_type = None

    wt.save()


def get_employees_very_first():
    """
    Ошибка с потерей данных в словаре у very_first_data
    :return:
    """
    full_data = []
    very_first_emps = models.VeryFirst.objects.values()
    print('very_first_emps', very_first_emps)
    for very_first_data in very_first_emps:
        print('\n\n', very_first_data)
        vf_data = models.VeryFirst.objects.filter(id__veryfirst=very_first_data['id_id']).values()
        emp_data = models.Employees.objects.filter(id=very_first_data['id_id']).values()
        full_data.append({'very_first_data': list(vf_data),
                          'emp_data': list(emp_data)})
        print(full_data)
    return full_data


def get_active_cities():
    cities = models.City.objects.filter(active=1).values()
    return list(cities)


def get_emp_ammount_in_cities():
    data = {}
    cities = models.City.objects.filter(active=1).values('id', 'city')
    work_types = models.WorkType.objects.filter(active=1).values('id', 'type')

    for city in cities:
        wt_data = {}
        for wt in work_types:
            emps_ammount = models.Employees.objects.filter(id_city=city['id'],
                                                   employeesworktype__id_work_type=wt['id']).aggregate(Count('id'))['id__count']
            wt_data.update({wt['id']: emps_ammount})
        data.update({city['id']: wt_data})
    return data


def add_new_work_type(name, step_0, step_1, step_2, step_3, step_4, step_5):
    new_wt = models.WorkType(id_field=1, type=name,
                             comm_stage_0=step_0,
                             comm_stage_1=step_1,
                             comm_stage_2=step_2,
                             comm_stage_3=step_3,
                             comm_stage_4=step_4,
                             comm_stage_5=step_5,
                             )
    new_wt.save()


def get_emp_ammount_wt(exclusive=False, active=False):
    data = {}
    emps = []
    if exclusive:
        emp_dict = models.Employees.objects.filter(exclusive=1).values('id')
    elif active:
        emp_dict = models.Employees.objects.filter(active=1).values('id')
    else:
        return 'err'
    for e in emp_dict:
        emps.append(e['id'])
    work_types = models.WorkType.objects.filter(active=1).values('id', 'type')
    for wt in work_types:
        count = 0
        emp_with_wt = []
        emp_with_wt_dict = models.EmployeesWorkType.objects.filter(id_work_type=wt['id']).values('id_user')
        for emp in emp_with_wt_dict:
            emp_with_wt.append(emp['id_user'])
        for emp in emp_with_wt:
            if emp in emps:
                count += 1
        data.update({wt['id']: count})
    return data


def get_online_ammount_wt():
    data = {}
    excl = []
    excl_dict = models.Employees.objects.filter(active=1).values('id')
    for excl in excl_dict:
        excl.append(excl_dict['id'])
    work_types = models.WorkType.objects.filter(active=1).values('id', 'type')
    for wt in work_types:
        count = 0
        emp_with_wt = []
        emp_with_wt_dict = models.EmployeesWorkType.objects.filter(id_work_type=wt['id']).values('id_user')
        for emp in emp_with_wt_dict:
            emp_with_wt.append(emp['id_user'])
        for emp in emp_with_wt:
            if emp in excl:
                count += 1
        data.update({wt['id']: count})
    return data


# def get_employees(id_status=None, id_city=None, number=None, id_user=None,
#                   id_work_type=None, not_null_balance=None, very_first=None, exclusive=None, is_active=None,
#                   negative_balance=None, reg_today=None, proped=None):
#     """
#     Получить исполнителей по статусу и отрасли
#     """
#     # print('number', number)
#     from django.db import connection
#     cursor = connection.cursor()
#     employees_list = []
#     sql = 'SELECT emp.id, emp.mail, emp.promo_id, emp.executor_type as id_executor, ' \
#           'ex.type as executor_type, emp.id_city, c.city, emp.full_name as fio, ' \
#           'emp.phone, emp.exclusive, emp.status as id_status, su.status_type as status, emp.comment, emp.about_us, ' \
#           'DATE_FORMAT(emp.reg_date, %s) as reg_date, emp.active, emp.balance, emp.bonuses ' \
#           'FROM employees emp ' \
#           'JOIN employees_work_type ewt ON emp.id=ewt.id_user ' \
#           'LEFT JOIN work_type wt ON ewt.id_work_type=wt.id ' \
#           'LEFT JOIN field_of_activity foa ON foa.id=wt.id_field ' \
#           'LEFT JOIN executor ex ON emp.executor_type=ex.id ' \
#           'LEFT JOIN city c ON emp.id_city=c.id ' \
#           'LEFT JOIN status_user su ON emp.status=su.id ' \
#           'WHERE c.active=1 '
#     if id_user is not None:
#         sql += 'AND emp.id={} '.format(id_user)
#     if id_status is not None:
#         sql += 'AND emp.status={} '.format(id_status)
#     if id_city is not None:
#         sql += 'AND emp.id_city={} '.format(id_city)
#     if id_work_type is not None:
#         sql += 'AND ewt.id_work_type={} '.format(id_work_type)
#     if not_null_balance is not None:
#         sql += 'AND emp.balance>0 '
#     if exclusive is not None:
#         sql += 'AND emp.exclusive=1 '
#     if negative_balance is not None:
#         sql += 'AND emp.balance<0 '
#     if is_active is not None:
#         sql += 'AND emp.active=1 '
#     if reg_today is not None:
#         sql += 'AND reg_date=CURDATE()'
#     if number is not None:
#         number = '%' + str(int(''.join(filter(str.isdigit, number))))[-10:]
#         if len(number) == 11:
#             employees = dictfetchall(cursor.execute(sql + 'AND emp.phone LIKE {} GROUP BY emp.id',
#                                                     '%m.%d.%y'.format(number)))
#         else:
#             return []
#     else:
#         sql += 'GROUP BY emp.id'
#         employees = dictfetchall(cursor.execute(sql))
#     num = 0
#     for emp in employees:
#         num += 1
#         # work_types = execute('SELECT ewt.id_work_type, wt.type as work_type FROM employees_work_type ewt '
#         #                      'RIGHT JOIN work_type wt ON ewt.id_work_type=wt.id '
#         #                      'WHERE ewt.id_user=%(p)s', emp['id'])
#         work_types = get_work_types(id_field)
#         # print(work_types)
#         work_types_list = []
#         for wt in work_types:
#             if cursor.execute('SELECT * FROM employees_work_type WHERE `id_user`=%s AND `id_work_type`=%s',
#                        [emp['id'], wt['id']]):
#                 work_types_list.append(
#                     {
#                         'id_work_type': wt['id'],
#                         'work_type': wt['type'],
#                         'active': 1
#                     })
#             else:
#                 work_types_list.append(
#                     {
#                         'id_work_type': wt['id'],
#                         'work_type': wt['type'],
#                         'active': 0
#                     })
#         successful_deals_count = dictfetchall(cursor.execute('SELECT COUNT(*) as sd_count '
#                                          'FROM deals WHERE id_user=%s AND status=4', [emp['id']]))
#         drop_deals_count = dictfetchall(cursor.execute('SELECT COUNT(*) as dd_count '
#                                    'FROM deals WHERE id_user=%s AND status=-1', [emp['id']]))
#         sum_commissions = dictfetchall(cursor.execute('SELECT SUM(commission) as sum_commissions '
#                                   'FROM deals WHERE id_user=%s', [emp['id']]))
#         drop_deal = dictfetchall(cursor.execute('SELECT d.id, d.title, d.phone, sd.status_type as status, d.comment, '
#                             'DATE_FORMAT(d.date_drop, %s) as date_drop, wt.type '
#                             'FROM deals d '
#                             'LEFT JOIN status_deal sd ON d.status=sd.id '
#                             'LEFT JOIN work_type wt ON d.id_work_type=wt.id '
#                             'WHERE id_user=%s AND status=-1 '
#                             'ORDER BY date_drop DESC LIMIT 1', '%m.%d.%y %H:%i', [emp['id']]))
#         deals = dictfetchall(cursor.execute('SELECT FORMAT(@i:=@i+1,0) AS num, d.id, d.title, d.description, d.price, d.value, '
#                         'd.address, d.phone, DATE_FORMAT(d.date, %s) as date, d.commission, d.commission_precent, '
#                         'sd.status_type as status, d.self_employeed, '
#                         'd.money_on_balance, d.comment, wt.type '
#                         'FROM (select @i:=0) AS iter, deals d '
#                         'LEFT JOIN status_deal sd ON d.status=sd.id '
#                         'LEFT JOIN work_type wt ON d.id_work_type=wt.id '
#                         'WHERE id_user=%s', '%m.%d.%y %H:%i', [emp['id']]))
#
#         very_fist_list = dictfetchall(cursor.execute('SELECT `id_user` from `very_first`'))
#         full_list = []
#         for item in range(0, very_fist_list.__len__()):
#             full_list.append(very_fist_list[item]['id_user'])
#         if drop_deal:
#             drop_deal = drop_deal[0]
#         if very_fist_list:
#             if emp['id'] in full_list:
#                 vf = '+'
#             else:
#                 vf = '-'
#         else:
#             vf = '-'
#         employees_list.append(
#             {
#                 'num': num,
#                 'id': emp['id'],
#                 'id_executor': emp['id_executor'],
#                 'executor_type': emp['executor_type'],
#                 'id_city': emp['id_city'],
#                 'promo_id': emp['promo_id'],
#                 'city': emp['city'],
#                 'fio': emp['fio'],
#                 'phone': emp['phone'],
#                 'mail': emp['mail'],
#                 'id_status': emp['id_status'],
#                 'status': emp['status'],
#                 'exclusive': emp['exclusive'],
#                 'comment': emp['comment'],
#                 'about_us': emp['about_us'],
#                 'reg_date': emp['reg_date'],
#                 'balance': emp['balance'],
#                 'bonuses': emp['bonuses'],
#                 'active': emp['active'],
#                 'very_first': vf,
#                 'successful_deals': successful_deals_count,
#                 'drop deals': drop_deals_count,
#                 'sum_commissions': sum_commissions,
#                 'work_types': work_types_list,
#                 'drop_deal': drop_deal,
#                 'deals': deals
#             })
#     # print(employees_list)
#     return employees_list
#



def get_active_masters_info(wt=None, city=None, exclusive=None, active=None,
                            vf=None, freeze=None, blocked=None, negative_balance=None,
                            positive_balance=None, registered_today=None):
    emp_info = []
    emps = models.Employees.objects.all().filter(status=1)
    if wt:
        emps = emps.filter(employeesworktype__id_work_type=wt)
    if city:
        emps = emps.filter(id_city=city)
    if exclusive:
        emps = emps.filter(exclusive=1)
    if active:
        emps = emps.filter(active=1)
    if freeze:
        emps = emps.filter(status=2)
    if blocked:
        emps = emps.filter(status=3)
    if blocked:
        emps = emps.filter(status=3)
    if negative_balance:
        emps = emps.filter(balance__lte=0)
    if positive_balance:
        emps = emps.filter(balance__gt=0)
    if registered_today:
        emps = emps.filter(reg_date=datetime.datetime.date.today)
    for emp in emps.values():
        if vf:
            if list(models.VeryFirst.objects.filter(id=emp['id']).values()) == []:
                continue
        referal_income = models.Employees.objects.all().filter(promo_id=emp['id']).aggregate(Count('promo_id'))['promo_id__count'] * 250
        proped_deals_count = models.Deals.objects.all().filter(id_proped=emp['id'], status=4).aggregate(Count('id_proped'))['id_proped__count']
        closed_deals_count = models.Deals.objects.all().filter(id_user=emp['id'], status=4).aggregate(Count('id_user'))['id_user__count']
        droped_deals_count = models.Deals.objects.all().filter(id_user=emp['id'], status=-1).aggregate(Count('id_user'))['id_user__count']
        if list(models.VeryFirst.objects.filter(id=emp['id']).values()) == []:
            very_first = None
        else:
            very_first = 1
        emp_wt = []
        for wt in get_emp_wt(emp['id']):
            emp_wt.append(wt['id_work_type_id'])
        emp_info.append(
            {
                'id': emp['id'],
                'full_name': emp['full_name'],
                'emp_wt': emp_wt,
                'id_city': emp['id_city'],
                'name_city': models.City.objects.filter(id=emp['id_city']).values('city')[0]['city'],
                'reg_date': emp['reg_date'],
                'phone': emp['phone'],
                'balance': emp['balance'],
                'bonuses': emp['bonuses'],
                'exclusive': emp['exclusive'],
                'active': emp['active'],
                'very_first': very_first,
                'referal_income': referal_income,
                'proped_deals_count': proped_deals_count,
                'closed_deals_count': closed_deals_count,
                'droped_deals_count': droped_deals_count
            }
        )

    return emp_info


def get_emp_wt(master_id):
    wt = models.EmployeesWorkType.objects.filter(id_user=master_id).values('id_work_type_id')
    return wt


def get_emp_wt_list(master_id):
    emp_wt = []
    for wt in get_emp_wt(master_id):
        emp_wt.append(wt['id_work_type_id'])
    return emp_wt


def edit_emp(master_id, full_name, phone, wt_list, excl):
    cursor = connection.cursor()
    master = models.Employees.objects.get(id=master_id)
    master.full_name = full_name
    master.phone = phone
    models.EmployeesWorkType.objects.filter(id_user_id=master_id).delete()
    if excl == 'on':
        master.exclusive = 1
    else:
        master.exclusive = None
    for wt in wt_list:
        cursor.execute('INSERT INTO employees_work_type(id_user, id_work_type) '
                                                     'VALUES (%s, %s)', [master_id, int(wt)])
        connection.commit()
    master.save()


def get_not_registered_masters():
    full_data = []
    emp_data = models.Employees.objects.filter(status=0).values()
    for emp in emp_data:
        wt_list = []
        wt = models.EmployeesWorkType.objects.filter(id_user=emp['id']).values('id_work_type_id')
        for i in wt:
            wt_list.append(i['id_work_type_id'])
        full_data.append(
            {
                'emp_data': emp,
                'emp_wt': wt_list,
            }
        )
    return full_data


def freeze_emp(emp_id):
    emp = models.Employees.objects.get(id=emp_id)
    emp.status = -1
    emp.save()


def add_emp(emp_id, wt_data):
    emp = models.Employees.objects.get(id=emp_id)
    emp.status = 1
    emp.save()
    print(wt_data)
    for wt_id in wt_data:
        print(wt_id, '\n')
        try:
            wt = models.EmployeesWorkType(id_user=models.Employees.objects.get(id=emp_id),
                                          id_work_type=models.WorkType.objects.get(id=wt_id))
            wt.save()
        except Exception as e:
            print(e)


def create_operator(name, token):
    try:
        operator_auth = User.objects.create_user(username=name, password=token)
        operator_data = models.Operators(id=operator_auth.id, name=name, token=token)
        operator_auth.save()
        operator_data.save()
        return True
    except Exception:
        return False


def get_operators():
    data = []
    data = {
        'operator_data': models.Operators.objects.all().values(),
        'auth_data': User.objects.all().filter(is_superuser=0).values()
    }
    return data


def delete_operator(operator_id):
    try:
        operator_data = models.Operators.objects.get(id=operator_id)
        operator_auth = User.objects.get(id=operator_id)
        operator_data.delete()
        operator_auth.delete()
        return True
    except Exception:
        return False


def get_wt_list():
    return models.WorkType.objects.all().values()


def get_master_card_info(master_id):
    user_data = models.Employees.objects.all().filter(id=master_id).values()
    users_deals = models.Deals.objects.all().filter(id_user=master_id).values()
    users_referal = models.Employees.objects.all().filter(promo_id=master_id).values('id', 'balance')
    for user in users_referal:
        deals_ammount = models.Deals.objects.all().filter(id_user=master_id).aggregate(Count('id'))['id__count']
        user.update({'deals_ammount': deals_ammount})
    users_session_history = models.UserSessionHistory.objects.all().filter(id=master_id).values()
    users_transfers = models.UsersTransfers.objects.all().filter(id_user=master_id).values()

    return {
        'id': master_id,
        'work_types': list(get_emp_wt(master_id)),
        'city': models.City.objects.all().filter(id=user_data[0]['id_city']).values('city')[0]['city'],
        'user_data': list(user_data),
        'deals': list(users_deals),
        'deals_len': list(users_deals).__len__(),
        'proped_deals_ammount': models.Deals.objects.filter(id_proped=master_id).aggregate(Count('id_proped'))['id_proped__count'],
        'referal': list(users_referal),
        'sessions':  list(users_session_history),
        'transfers': list(users_transfers),
    }

def get_active_deals():
    return models.Deals.objects.all().filter(status=1).values()

def get_history():
    return models.UsersHistory.objects.all().values()





def get_clients():
    return models.Client.objects.all().values()