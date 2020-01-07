from . import models
from django.db.models import Sum
import datetime
from datetime import date, timedelta



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


def get_sum_proped_by_date(start_date=date.today() - timedelta(days=31), end_date=date.today()):
    """
    Доход по предложенным сделкам по датам
    :param start_date:
    :param end_date:
    :return:
    """
    sum = 0
    proped_ids = models.PropedDeals.objects.values('deal_id')
    print(proped_ids)
    for id in proped_ids:
        comm = models.Deals.objects.filter(date_filing__gte=start_date,
                                           date_filing__lte=end_date,
                                           id=id['deal_id']).aggregate(Sum('commission'))
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
    sum = models.Employees.objects.filter(exclusive__exact=1).aggregate(Sum('balance'))
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
                'post_pay': wt['post_pay']
            })
    print(directions)
    return directions


def get_employees_very_first():
    """
    Ошибка с потерей данных в словаре у very_first_data
    :return:
    """
    full_data = []
    very_first_emps = models.VeryFirst.objects.values()
    print(very_first_emps)
    for very_first_data in very_first_emps:
        print('\n\n', very_first_data)
        vf_data = models.VeryFirst.objects.filter(id_user=very_first_data['id_user']).values()
        emp_data = models.Employees.objects.filter(id=very_first_data['id_user']).values()
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
            count = 0
            emp_in_city = []
            emp_with_wt = []
            emp_in_city_dict = models.Employees.objects.filter(id_city=city['id']).values('id')
            for emp in emp_in_city_dict:
                emp_in_city.append(emp['id'])
            emp_with_wt_dict = models.EmployeesWorkType.objects.filter(id_work_type=wt['id']).values('id_user')
            for emp in emp_with_wt_dict:
                emp_with_wt.append(emp['id_user'])
            for emp in emp_with_wt:
                if emp in emp_in_city:
                    count += 1
            wt_data.update({wt['id']: count})
        data.update({city['id']: wt_data})
    return data


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

def get_employees(id_field, id_status=None, id_city=None, number=None, id_user=None,
                  id_work_type=None, not_null_balance=None, very_first=None, exclusive=None, is_active=None,
                  negative_balance=None, reg_today=None, proped=None):
    """
    Получить исполнителей по статусу и отрасли
    """
    # print('number', number)
    employees_list = []
    sql = 'SELECT emp.id, emp.mail, emp.promo_id, emp.executor_type as id_executor, ' \
          'ex.type as executor_type, emp.id_city, c.city, emp.full_name as fio, ' \
          'emp.phone, emp.exclusive, emp.status as id_status, su.status_type as status, emp.comment, emp.about_us, ' \
          'DATE_FORMAT(emp.reg_date, %(p)s) as reg_date, emp.active, emp.balance, emp.bonuses ' \
          'FROM employees emp ' \
          'JOIN employees_work_type ewt ON emp.id=ewt.id_user ' \
          'LEFT JOIN work_type wt ON ewt.id_work_type=wt.id ' \
          'LEFT JOIN field_of_activity foa ON foa.id=wt.id_field ' \
          'LEFT JOIN executor ex ON emp.executor_type=ex.id ' \
          'LEFT JOIN city c ON emp.id_city=c.id ' \
          'LEFT JOIN status_user su ON emp.status=su.id ' \
          'WHERE wt.id_field={} AND c.active=1 '.format(id_field)
    if id_user is not None:
        sql += 'AND emp.id={} '.format(id_user)
    if id_status is not None:
        sql += 'AND emp.status={} '.format(id_status)
    if id_city is not None:
        sql += 'AND emp.id_city={} '.format(id_city)
    if id_work_type is not None:
        sql += 'AND ewt.id_work_type={} '.format(id_work_type)
    if not_null_balance is not None:
        sql += 'AND emp.balance>0 '
    if exclusive is not None:
        sql += 'AND emp.exclusive=1 '
    if negative_balance is not None:
        sql += 'AND emp.balance<0 '
    if is_active is not None:
        sql += 'AND emp.active=1 '
    if reg_today is not None:
        sql += 'AND reg_date=CURDATE()'
    if number is not None:
        number = '%' + str(int(''.join(filter(str.isdigit, number))))[-10:]
        if len(number) == 11:
            employees = models.Employees.objects.raw(sql + 'AND emp.phone LIKE  %(p)s GROUP BY emp.id', '%m.%d.%y', number)
        else:
            return []
    else:
        sql += 'GROUP BY emp.id'
        employees = models.Employees.objects.raw(sql, '%m.%d.%y')
    num = 0
    for emp in employees:
        num += 1
        # work_types = execute('SELECT ewt.id_work_type, wt.type as work_type FROM employees_work_type ewt '
        #                      'RIGHT JOIN work_type wt ON ewt.id_work_type=wt.id '
        #                      'WHERE ewt.id_user=%(p)s', emp['id'])
        work_types = get_work_types(id_field)
        # print(work_types)
        work_types_list = []
        for wt in work_types:
            if execute('SELECT * FROM employees_work_type WHERE `id_user`=%(p)s AND `id_work_type`=%(p)s',
                       emp['id'], wt['id']):
                work_types_list.append(
                    {
                        'id_work_type': wt['id'],
                        'work_type': wt['type'],
                        'active': 1
                    })
            else:
                work_types_list.append(
                    {
                        'id_work_type': wt['id'],
                        'work_type': wt['type'],
                        'active': 0
                    })
        successful_deals_count = execute('SELECT COUNT(*) as sd_count '
                                         'FROM deals WHERE id_user=%(p)s AND status=4', emp['id'])[0]['sd_count']
        drop_deals_count = execute('SELECT COUNT(*) as dd_count '
                                   'FROM deals WHERE id_user=%(p)s AND status=-1', emp['id'])[0]['dd_count']
        sum_commissions = execute('SELECT SUM(commission) as sum_commissions '
                                  'FROM deals WHERE id_user=%(p)s', emp['id'])[0]['sum_commissions']
        drop_deal = execute('SELECT d.id, d.title, d.phone, sd.status_type as status, d.comment, '
                            'DATE_FORMAT(d.date_drop, %(p)s) as date_drop, wt.type '
                            'FROM deals d '
                            'LEFT JOIN status_deal sd ON d.status=sd.id '
                            'LEFT JOIN work_type wt ON d.id_work_type=wt.id '
                            'WHERE id_user=%(p)s AND status=-1 '
                            'ORDER BY date_drop DESC LIMIT 1', '%m.%d.%y %H:%i', emp['id'])
        deals = execute('SELECT FORMAT(@i:=@i+1,0) AS num, d.id, d.title, d.description, d.price, d.value, '
                        'd.address, d.phone, DATE_FORMAT(d.date, %(p)s) as date, d.commission, d.commission_precent, '
                        'sd.status_type as status, d.self_employeed, '
                        'd.money_on_balance, d.comment, wt.type '
                        'FROM (select @i:=0) AS iter, deals d '
                        'LEFT JOIN status_deal sd ON d.status=sd.id '
                        'LEFT JOIN work_type wt ON d.id_work_type=wt.id '
                        'WHERE id_user=%(p)s', '%m.%d.%y %H:%i', emp['id'])

        very_fist_list = execute('SELECT `id_user` from `very_first`')
        full_list = []
        for item in range(0, very_fist_list.__len__()):
            full_list.append(very_fist_list[item]['id_user'])
        if drop_deal:
            drop_deal = drop_deal[0]
        if very_fist_list:
            if emp['id'] in full_list:
                vf = '+'
            else:
                vf = '-'
        else:
            vf = '-'
        employees_list.append(
            {
                'num': num,
                'id': emp['id'],
                'id_executor': emp['id_executor'],
                'executor_type': emp['executor_type'],
                'id_city': emp['id_city'],
                'promo_id': emp['promo_id'],
                'city': emp['city'],
                'fio': emp['fio'],
                'phone': emp['phone'],
                'mail': emp['mail'],
                'id_status': emp['id_status'],
                'status': emp['status'],
                'exclusive': emp['exclusive'],
                'comment': emp['comment'],
                'about_us': emp['about_us'],
                'reg_date': emp['reg_date'],
                'balance': emp['balance'],
                'bonuses': emp['bonuses'],
                'active': emp['active'],
                'very_first': vf,
                'successful_deals': successful_deals_count,
                'drop deals': drop_deals_count,
                'sum_commissions': sum_commissions,
                'work_types': work_types_list,
                'drop_deal': drop_deal,
                'deals': deals
            })
    # print(employees_list)
    return employees_list