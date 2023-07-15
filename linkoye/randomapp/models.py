from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here.

STATUS_CHOICES = [
    ('completed', 'COMPLETED'),
    ('to do', 'TO DO'),
]

class Site_Selling_Category(models.Model):
    Category_Name = models.CharField(max_length = 100)

    def __str__(self):
        return self.Category_Name

class User_Profile(models.Model):
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    contact = models.CharField(max_length=11)
    skype = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    company = models.CharField(max_length=300)
    VAT = models.DecimalField(max_digits = 10,decimal_places = 2, null =True, blank=True)
    website = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return str(self.user)


class Services(models.Model):
    Thumbnail = models.ImageField(upload_to ='Service_Thumbnail')
    Service_Title = models.CharField(max_length = 200)
    Description = models.TextField()

class Blogs(models.Model):
    Thumbnail = models.ImageField(upload_to ='Service_Thumbnail')
    Blog_Title = models.CharField(max_length = 200)
    Author = models.CharField(max_length=200)
    Description = RichTextField()


class Sites(models.Model):
    URL = models.CharField(max_length = 300)
    Image = models.ImageField(blank=True, null=True)
    DA = models.IntegerField()
    PA = models.IntegerField()
    Organic_Traffic = models.IntegerField()
    Link_Allowed = models.IntegerField()
    Link_Type = models.CharField(max_length = 200)
    Country = models.CharField(max_length = 100)
    Language = models.CharField(max_length = 100)
    Image_Allowed = models.IntegerField()
    Description =models.TextField()
    # Description = models.TextField()
    Restricted_Topics = models.TextField()
    Selling_Category = models.ForeignKey(Site_Selling_Category, on_delete=models.CASCADE, blank = True, null = True)
    Price = models.DecimalField(max_digits = 10,decimal_places = 2)


class Link_Category(models.Model):
    Link_Type = models.CharField(max_length = 300)

    def __str__(self):
        return self.Link_Type

class Order_Details(models.Model):
    PAID_CHOICES = [
        ('paid', 'Paid'),
        ('not paid', 'Not Paid'),
    ]

    PAYMENT_WAYS =[
        ('wallet credit', 'Wallet Credit'),
        ('bank transfer', 'Bank Transfer'),
    ]
    Order_ID = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Order_Total = models.DecimalField(max_digits = 10,decimal_places = 2)
    Payment_Method = models.CharField(max_length=20, choices=PAYMENT_WAYS, default = 'wallet credit')
    Paid = models.CharField(max_length=10, choices=PAID_CHOICES, default='not paid')

    def __str__(self):
        return str(self.Order_ID)

class Order_Request(models.Model):
    Order_ID = models.ForeignKey(Order_Details, on_delete = models.CASCADE)
    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    URL = models.CharField(max_length = 300)
    Title = models.CharField(max_length = 300)
    Order_Date = models.DateField()
    Order_Deadline = models.DateField()
    keywords = models.TextField()
    urls = models.TextField()
    link_Type = models.CharField(max_length = 300)
    details = RichTextField()
    image_url = models.TextField()
    terms_to_avoid = models.TextField()
    info_source = models.TextField()
    Price = models.DecimalField(max_digits = 10,decimal_places = 2)
    Status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default='to do')
    Completion_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.Order_ID)
    

class Billing_Details(models.Model):
    Order_ID = models.ForeignKey(Order_Details, on_delete = models.CASCADE, null=False)
    Country = models.CharField(max_length = 300)
    First_Name = models.CharField(max_length = 300)
    Last_Name = models.CharField(max_length = 300)
    Company_Name = models.CharField(max_length = 300, null=True)
    VAT = models.CharField(max_length = 300, null=True, blank= True)
    Address = models.TextField()
    City = models.CharField(max_length = 300)
    State = models.CharField(max_length = 300, null=True)
    Zip_Code = models.IntegerField()
    Email = models.CharField(max_length = 300)
    Phone = models.CharField(max_length = 300)
    Order_Notes = models.TextField(null=True)


class WalletTransaction(models.Model):
    PENDING = 'pending'
    SUCCESS = 'success'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SUCCESS, 'Success'),
        (FAILED, 'Failed'),
    ]

    order_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    IBAN = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_id



class UserCredit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.credit)


class BankDetails(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'usd'),
        ('EUR', 'eur'),
        ('POUND', 'pound'),
    ]
    currency = models.CharField(max_length=20, choices=CURRENCY_CHOICES, default= 'usd')
    account_holder_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=200)
    # ACH_Routing = models.CharField(max_length=200)
    IBAN = models.CharField(max_length=100)
    note = models.TextField()
    File = models.FileField(upload_to='Bank Detail')
