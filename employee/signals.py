from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.conf import settings

from .models import Employee, MyLog


# this receiver is executed every-time some data is saved in any table
# @receiver(pre_save, sender=Employee)
# def audit_log(sender, instance, **kwargs):
#     # code to execute before every model save
#     print("Inside signal code")

@receiver(pre_save, sender=Employee)
def save_model_changes(sender, instance, **kwargs):

    try:
        table_pk = instance._meta.pk.name
        table_pk_value = instance.__dict__[table_pk]
        query_kwargs = dict()
        query_kwargs[table_pk] = table_pk_value
        prev_instance = sender.objects.get(**query_kwargs)  # for dynamic column name

        # print(prev_instance)
        # # print(user.first_name)
        # print(str(instance._meta.db_table))

        # existing_employee = Employee.objects.get(id=prev_instance.pk)
        # msg = ''
        # changed_fields = existing_employee.get_dirty_filds()
        # print(changed_fields)
        # if existing_employee.is_dirty():
        #     changed_fields = existing_employee.get_dirty_filds()
        #     print(changed_fields)
        #     for key in changed_fields:
        #         msg = msg + key + ' value changes from ' + changed_fields[key] + ' to new value'

        log_data = MyLog(table_name=str(instance._meta.db_table), table_row= prev_instance.pk, timestamp= datetime.now())
        log_data.save()


    except ObjectDoesNotExist as e:
        # this instance is being created and not updated. ignore and return
        # logging.getLogger("info_logger").info("Signals: creating new instance of " + str(sender))
        return
