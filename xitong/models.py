from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500,null=True,default="");
    username = models.CharField(max_length=500,null=True,default="");
    password = models.CharField(max_length=500,null=True,default="");
    email = models.CharField(max_length=500,null=True,default="");
    managearea = models.CharField(max_length=500,null=True,default="");
class User(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500,null=True,default="");
    username = models.CharField(max_length=500,null=True,default="");
    password = models.CharField(max_length=500,null=True,default="");
    birthday = models.CharField(max_length=500,null=True,default="");
    sex = models.CharField(max_length=500,null=True,default="");
    email = models.CharField(max_length=500,null=True,default="");
    homeaddress = models.CharField(max_length=500,null=True,default="");
    emercontact = models.CharField(max_length=500,null=True,default="");
    bankcard = models.CharField(max_length=500,null=True,default="");
    payslip = models.CharField(max_length=500,null=True,default="");
class Repairman(models.Model):
    id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500,null=True,default="");
    username = models.CharField(max_length=500,null=True,default="");
    password = models.CharField(max_length=500,null=True,default="");
    email = models.CharField(max_length=500,null=True,default="");
    address = models.CharField(max_length=500,null=True,default="");
    allowtype = models.CharField(max_length=500,null=True,default="");
    state = models.CharField(max_length=500,null=True,default="");
    bankcard = models.CharField(max_length=500,null=True,default="");
    payslip = models.CharField(max_length=500,null=True,default="");
class Serviceorder(models.Model):
    id = models.AutoField(primary_key=True);
    user = models.CharField(max_length=500,null=True,default="");
    userid = models.CharField(max_length=500,null=True,default="");
    price = models.CharField(max_length=500,null=True,default="");
    substate = models.CharField(max_length=500,null=True,default="");
    chargetype = models.CharField(max_length=500,null=True,default="");
    paytype = models.CharField(max_length=500,null=True,default="");
class Car(models.Model):
    id = models.AutoField(primary_key=True);
    carnumber = models.CharField(max_length=500,null=True,default="");
    type = models.CharField(max_length=500,null=True,default="");
    firm = models.CharField(max_length=500,null=True,default="");
    model = models.CharField(max_length=500,null=True,default="");
    caryear = models.CharField(max_length=500,null=True,default="");
    color = models.CharField(max_length=500,null=True,default="");
    user = models.CharField(max_length=500,null=True,default="");
    userid = models.CharField(max_length=500,null=True,default="");
class Rescueorder(models.Model):
    id = models.AutoField(primary_key=True);
    ordernumber = models.CharField(max_length=500,null=True,default="");
    user = models.CharField(max_length=500,null=True,default="");
    userid = models.CharField(max_length=500,null=True,default="");
    car = models.CharField(max_length=500,null=True,default="");
    carid = models.CharField(max_length=500,null=True,default="");
    troubletype = models.CharField(max_length=500,null=True,default="");
    rescaddress = models.CharField(max_length=500,null=True,default="");
    troubledesc = models.CharField(max_length=500,null=True,default="");
    reason = models.CharField(max_length=500,null=True,default="");
    orderstate = models.CharField(max_length=500,null=True,default="");
    precost = models.CharField(max_length=500,null=True,default="");
    predate = models.CharField(max_length=500,null=True,default="");
    duration = models.CharField(max_length=500,null=True,default="");
    repairman = models.CharField(max_length=500,null=True,default="");
    repairmanid = models.CharField(max_length=500,null=True,default="");
class Ordereval(models.Model):
    id = models.AutoField(primary_key=True);
    rescueorder = models.CharField(max_length=500,null=True,default="");
    rescueorderid = models.CharField(max_length=500,null=True,default="");
    content = models.CharField(max_length=500,null=True,default="");
    addtime = models.CharField(max_length=500,null=True,default="");
    user = models.CharField(max_length=500,null=True,default="");
    userid = models.CharField(max_length=500,null=True,default="");
class Schedule(models.Model):
    id = models.AutoField(primary_key=True);
    repairman = models.CharField(max_length=500,null=True,default="");
    repairmanid = models.CharField(max_length=500,null=True,default="");
    content = models.CharField(max_length=500,null=True,default="");
    plandate = models.CharField(max_length=500,null=True,default="");
    state = models.CharField(max_length=500,null=True,default="");


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
    first_name = models.CharField(max_length=150)
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