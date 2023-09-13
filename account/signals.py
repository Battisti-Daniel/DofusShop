from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from account.models import Account, AccountAmount, ItemAmount, Item
from django.db.models import Sum


@receiver(post_save, sender=Account)
def account_post_save(sender, instance, created, **kwargs):
    if created:
        account_count = Account.objects.all().count()
        AccountAmount.objects.create(account_create=account_count)


@receiver(post_delete, sender=Account)
def account_post_delete(sender, instance, **kwargs):
    account_count = Account.objects.all().count()
    AccountAmount.objects.create(account_create=account_count)


@receiver(post_save, sender=Item)
def item_post_save(sender, instance, created, **kwargs):
    if created:
        item_count = Item.objects.all().count()

        total_value = Item.objects.aggregate(total_value=(Sum('value')))
        total_value = float(total_value['total_value'])

        ItemAmount.objects.create(
            name=instance,
            total_item=item_count,
            total_amount=total_value
        )

@receiver(post_delete, sender=Item)
def item_post_delete(sender, instance, **kwargs):

        item_count = Item.objects.all().count()

        total_value = Item.objects.aggregate(total_value=(Sum('value')))
        print(total_value)
        if total_value['total_value'] is None:
            total_value = 0.0
        else:
            total_value = float(total_value['total_value'])

        ItemAmount.objects.create(
            name=instance,
            total_item=item_count,
            total_amount=total_value
        )