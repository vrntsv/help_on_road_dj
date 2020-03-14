# Generated by Django 2.2.2 on 2020-01-06 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'all_transfer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AnswerMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'answer_message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('active', models.IntegerField()),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('discont', models.IntegerField(blank=True, null=True)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('model_auto', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField()),
                ('count_call', models.SmallIntegerField()),
                ('reg_date', models.DateTimeField()),
                ('last_time', models.DateTimeField(blank=True, null=True)),
                ('accept_message', models.IntegerField()),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommisionTimer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer', models.TimeField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('date_time_now', models.TimeField(blank=True, null=True)),
                ('time_difference', models.TimeField(blank=True, null=True)),
                ('time_for_stage_6', models.TimeField(blank=True, null=True)),
                ('client_timer', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'commision_timer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amo_key', models.CharField(max_length=255)),
                ('commission', models.IntegerField()),
            ],
            options={
                'db_table': 'config',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DealQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_deal', models.BigIntegerField()),
                ('question', models.TextField()),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'deal_questions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('model_auto', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=25)),
                ('date_filing', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('waittime', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField()),
                ('date_accept', models.DateTimeField(blank=True, null=True)),
                ('date_drop', models.DateTimeField(blank=True, null=True)),
                ('last_change_stage', models.TimeField(blank=True, null=True)),
                ('value', models.IntegerField()),
                ('money_on_balance', models.IntegerField()),
                ('current_stage', models.IntegerField()),
                ('commission_precent', models.IntegerField(blank=True, null=True)),
                ('commission', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('comment_master', models.TextField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('date_completion', models.DateTimeField(blank=True, null=True)),
                ('self_employeed', models.IntegerField()),
            ],
            options={
                'db_table': 'deals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('mail', models.CharField(blank=True, max_length=144, null=True)),
                ('exclusive', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('about_us', models.CharField(max_length=255)),
                ('reg_date', models.DateField(blank=True, null=True)),
                ('balance', models.IntegerField()),
                ('bonuses', models.IntegerField()),
                ('active', models.IntegerField()),
                ('days_with_zero_balance', models.SmallIntegerField()),
                ('promo_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeesWorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'employees_work_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_field', models.SmallIntegerField()),
                ('type', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'executor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FieldOfActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'field_of_activity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IdDealsMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_deal', models.BigIntegerField()),
                ('id_user', models.BigIntegerField()),
                ('id_message', models.BigIntegerField()),
            ],
            options={
                'db_table': 'id_deals_message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('time_send', models.DateTimeField()),
            ],
            options={
                'db_table': 'messages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewUsersWithSales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'new_users_with_sales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('token', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'operators',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PropedDeals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proped_user_id', models.IntegerField()),
                ('deal_id', models.IntegerField()),
            ],
            options={
                'db_table': 'proped_deals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatusDeal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status_type', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'status_deal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StatusUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status_type', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'status_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TopTimetable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('monday', models.CharField(blank=True, max_length=50, null=True)),
                ('tuesday', models.CharField(blank=True, max_length=50, null=True)),
                ('wednesday', models.CharField(blank=True, max_length=50, null=True)),
                ('thursday', models.CharField(blank=True, max_length=50, null=True)),
                ('friday', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'top_timetable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.BigIntegerField()),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'users_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersTransfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.BigIntegerField()),
                ('date', models.DateTimeField()),
                ('ammount', models.CharField(max_length=100)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('balance', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'users_transfers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VeryFirst',
            fields=[
                ('id_user', models.BigIntegerField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('tariff', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'very_first',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_field', models.IntegerField()),
                ('type', models.CharField(max_length=126, unique=True)),
                ('active', models.IntegerField()),
                ('comm_stage_0', models.SmallIntegerField()),
                ('comm_stage_1', models.SmallIntegerField()),
                ('comm_stage_2', models.SmallIntegerField()),
                ('comm_stage_3', models.SmallIntegerField()),
                ('comm_stage_4', models.SmallIntegerField()),
                ('comm_stage_5', models.SmallIntegerField()),
                ('comm_stage_6', models.SmallIntegerField()),
                ('post_pay', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'work_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserSessionHistory',
            fields=[
                ('id', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='site_backend.Employees')),
                ('date', models.DateField(blank=True, null=True)),
                ('start_session', models.TimeField(blank=True, null=True)),
                ('end_session', models.TimeField(blank=True, null=True)),
                ('long_session', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_session_history',
                'managed': False,
            },
        ),
    ]
