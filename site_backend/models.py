# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllTransfer(models.Model):
    id_user = models.ForeignKey('Employees', models.DO_NOTHING, db_column='id_user', primary_key=True)
    value = models.IntegerField()
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'all_transfer'


class AnswerMessage(models.Model):
    id_deals = models.ForeignKey('Deals', models.DO_NOTHING, db_column='id_deals')

    class Meta:
        managed = False
        db_table = 'answer_message'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    id_field = models.ForeignKey('FieldOfActivity', models.DO_NOTHING, db_column='id_field')
    city = models.CharField(max_length=100)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'city'
        unique_together = (('city', 'id_field'),)


class Client(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    discont = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    model_auto = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey('StatusUser', models.DO_NOTHING, db_column='status')
    active = models.IntegerField()
    count_call = models.SmallIntegerField()
    reg_date = models.DateField()
    last_time = models.DateTimeField(blank=True, null=True)
    accept_message = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client'


class CommisionTimer(models.Model):
    timer = models.TimeField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    date_time_now = models.TimeField(blank=True, null=True)
    time_difference = models.TimeField(blank=True, null=True)
    time_for_stage_6 = models.TimeField(blank=True, null=True)
    client_timer = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commision_timer'


class Config(models.Model):
    id_field = models.ForeignKey('FieldOfActivity', models.DO_NOTHING, db_column='id_field', unique=True)
    amo_key = models.CharField(max_length=255)
    commission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'config'


class DealQuestions(models.Model):
    id_deal = models.BigIntegerField()
    question = models.TextField()
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'deal_questions'


class Deals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_user = models.ForeignKey('Employees', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_work_type = models.ForeignKey('WorkType', models.DO_NOTHING, db_column='id_work_type')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    model_auto = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    date_filing = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    waittime = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    date_accept = models.DateField(blank=True, null=True)
    date_drop = models.DateField(blank=True, null=True)
    last_change_stage = models.TimeField(blank=True, null=True)
    value = models.IntegerField()
    money_on_balance = models.IntegerField()
    current_stage = models.IntegerField()
    commission_precent = models.IntegerField(blank=True, null=True)
    commission = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey('StatusDeal', models.DO_NOTHING, db_column='status')
    comment = models.TextField(blank=True, null=True)
    comment_master = models.TextField(blank=True, null=True)
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='id_city')
    price = models.CharField(max_length=100, blank=True, null=True)
    date_completion = models.DateTimeField(blank=True, null=True)
    self_employeed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deals'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    id = models.BigIntegerField(primary_key=True)
    executor_type = models.ForeignKey('Executor', models.DO_NOTHING, db_column='executor_type')
    id_city = models.ForeignKey(City, models.DO_NOTHING, db_column='id_city')
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    mail = models.CharField(max_length=144, blank=True, null=True)
    status = models.ForeignKey('StatusUser', models.DO_NOTHING, db_column='status')
    exclusive = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    about_us = models.CharField(max_length=255)
    reg_date = models.DateField(blank=True, null=True)
    balance = models.IntegerField()
    bonuses = models.IntegerField()
    active = models.IntegerField()
    days_with_zero_balance = models.SmallIntegerField()
    promo_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class EmployeesWorkType(models.Model):
    id_user = models.ForeignKey(Employees, models.DO_NOTHING, db_column='id_user', primary_key=True)
    id_work_type = models.ForeignKey('WorkType', models.DO_NOTHING, db_column='id_work_type')

    class Meta:
        managed = False
        db_table = 'employees_work_type'
        unique_together = (('id_user', 'id_work_type'),)


class Executor(models.Model):
    id_field = models.SmallIntegerField()
    type = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'executor'


class FieldOfActivity(models.Model):
    field = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'field_of_activity'


class IdDealsMessage(models.Model):
    id_deal = models.BigIntegerField()
    id_user = models.BigIntegerField()
    id_message = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'id_deals_message'


class Messages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    id_user = models.ForeignKey(Employees, models.DO_NOTHING, db_column='id_user')
    time_send = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'messages'


class NewUsersWithSales(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_users_with_sales'


class Operators(models.Model):
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'operators'


class PropedDeals(models.Model):
    proped_user_id = models.IntegerField()
    deal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proped_deals'


class StatusDeal(models.Model):
    id = models.IntegerField(primary_key=True)
    status_type = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'status_deal'


class StatusUser(models.Model):
    id = models.IntegerField(primary_key=True)
    status_type = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'status_user'


class TopTimetable(models.Model):
    id = models.AutoField(primary_key=True)
    monday = models.CharField(max_length=50, blank=True, null=True)
    tuesday = models.CharField(max_length=50, blank=True, null=True)
    wednesday = models.CharField(max_length=50, blank=True, null=True)
    thursday = models.CharField(max_length=50, blank=True, null=True)
    friday = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'top_timetable'


class UserSessionHistory(models.Model):
    id = models.ForeignKey(Employees, models.DO_NOTHING, db_column='id', primary_key=True)
    date = models.DateField(blank=True, null=True)
    start_session = models.TimeField(blank=True, null=True)
    end_session = models.TimeField(blank=True, null=True)
    long_session = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_session_history'


class UsersHistory(models.Model):
    id_user = models.BigIntegerField()
    date = models.DateTimeField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'users_history'


class UsersTransfers(models.Model):
    id_user = models.BigIntegerField()
    date = models.DateTimeField()
    ammount = models.CharField(max_length=100)
    comment = models.CharField(max_length=255, blank=True, null=True)
    balance = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users_transfers'


class VeryFirst(models.Model):
    id_user = models.BigIntegerField(primary_key=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    tariff = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'very_first'


class WorkType(models.Model):
    id_field = models.IntegerField()
    type = models.CharField(unique=True, max_length=126)
    active = models.IntegerField()
    comm_stage_0 = models.SmallIntegerField()
    comm_stage_1 = models.SmallIntegerField()
    comm_stage_2 = models.SmallIntegerField()
    comm_stage_3 = models.SmallIntegerField()
    comm_stage_4 = models.SmallIntegerField()
    comm_stage_5 = models.SmallIntegerField()
    comm_stage_6 = models.SmallIntegerField()
    post_pay = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_type'
