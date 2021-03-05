from django.db import models
from django.utils import timezone


class Member(models.Model):
    name = models.CharField(max_length=100, null=False)
    grade = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100)
    point = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def publish(self):
        self.updated_at = timezone.now()


class Item(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=100, null=False)
    barcode = models.IntegerField(blank=True)
    registered_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

    def publish(self):
        self.updated_at = timezone.now()


class Pay(models.Model):
    pay_way = models.CharField(max_length=100)
    point = models.IntegerField()
    price = models.IntegerField(null=False)
    pay_time = models.DateTimeField(default=timezone.now)
    refund = models.BooleanField(null=False, default=False)
    is_member = models.BooleanField(null=False, default=False)
    Member_id = models.ForeignKey(Member, related_name="member", on_delete=models.CASCADE)
    Item_id = models.ForeignKey(Item, related_name="item", on_delete=models.CASCADE)


class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=100)
    work_time = models.IntegerField(default=0)
    work_start = models.DateTimeField(default=timezone.now)
    birthday = models.DateField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

    def publish(self):
        self.updated_at = timezone.now()
