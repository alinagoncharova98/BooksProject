from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Count

User = get_user_model()


class CustomManager(models.Manager):
    def count_named_django(self):
        count_names = []
        named_django = self.get_queryset().aggregate(Count('name', filter='django'))
        others = self.get_queryset().aggregate(Count('name')) - named_django
        count_names.extend([named_django, others])
        return count_names


class Book(models.Model):
    # Поле id создаётся автоматически для каждой таблицы в БД и явл. PrimaryKey
    # id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    owner = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    # custom_manager = CustomManager()

    def __str__(self):
        return '%s %s' % (self.name, self.owner,)


@receiver(pre_save, sender=Book)
def change_name(sender, instance, **kwargs):
    if instance.name == 'test':
        instance.name = 'django'

