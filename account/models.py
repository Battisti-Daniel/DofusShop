from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    stars = models.PositiveIntegerField(default=0)
    authenticated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-created_at']


class AccountAmount(models.Model):
    account_create = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class TypeCharacteristic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Characteristic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typeCharacteristic = models.ForeignKey(TypeCharacteristic, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.typeCharacteristic}  {self.value}'


class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    characteristics = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='coverItem/')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


class ItemAmount(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    total_item = models.IntegerField()
