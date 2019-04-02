from django.db import models
# from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='/static/img/1')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Member(models.Model):
    member_email = models.CharField(max_length=200)
    member_pw = models.CharField(max_length=200)
    member_fname = models.CharField(max_length=200)
    member_lname = models.CharField(max_length=200)
    member_address = models.CharField(max_length=200)
    member_tel = models.CharField(max_length=200)

# -------------------------------------back end-----------------------------------------

class Goods(models.Model):
    goods_name = models.CharField(max_length=200)
    goods_price = models.IntegerField()
    goods_num = models.IntegerField()
    goods_detail = models.CharField(max_length=200)
    goods_photo = models.ImageField(upload_to='static/img/2')

# -------------------------------------back end-----------------------------------------

class Basket(models.Model):
    basket_email = models.CharField(max_length=200)
    basket_goods = models.CharField(max_length=200)
    basket_price = models.IntegerField()
    basket_num = models.IntegerField()

# -------------------------------------back end-----------------------------------------

class Shipment(models.Model):
    shipment_tax = models.CharField(max_length=200)
    shipment_date = models.CharField(max_length=200)
    shipment_time = models.CharField(max_length=200)
    shipment_sum = models.IntegerField()


# -------------------------------------back end-----------------------------------------



