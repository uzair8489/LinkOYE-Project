from django.contrib import admin
import datetime
from .models import *
# Register your models here.


class linkcategory_data(admin.ModelAdmin):
    list_display = ['Link_Type']

class userprofile_data(admin.ModelAdmin):
    list_display = ['user', 'contact', 'skype', 'address']

class services_data(admin.ModelAdmin):
    list_display = ['Service_Title', 'Thumbnail', 'Description']

class blogs_data(admin.ModelAdmin):
    list_display = ['Blog_Title', 'Thumbnail', 'Author']

class selling_category_data(admin.ModelAdmin):
    list_display = ['Category_Name']

class sites_data(admin.ModelAdmin):
    list_display = ['URL' , 'DA', 'PA', 'Organic_Traffic', 'Link_Allowed', 'Link_Type', 'Country', 'Language', 'Image_Allowed','Selling_Category', 'Price']

class billing_details(admin.ModelAdmin):
    list_display = ['Order_ID']

class WalletTransaction_data(admin.ModelAdmin):
    list_display = ('order_id', 'amount', 'created_at', 'updated_at')

class usercredit_data(admin.ModelAdmin):
    list_display = ('user', 'credit')

class bankdetails_data(admin.ModelAdmin):
    list_display = ('bank_name', 'account_holder_name', 'account_number', 'IBAN')

admin.site.register(Services,services_data)
admin.site.register(Sites, sites_data)
admin.site.register(Link_Category,linkcategory_data)
admin.site.register(Site_Selling_Category,selling_category_data)
admin.site.register(Blogs,blogs_data)
# admin.site.register(Order_Details)
# admin.site.register(Order_Request)
admin.site.register(User_Profile, userprofile_data)
admin.site.register(Billing_Details, billing_details)
admin.site.register(WalletTransaction, WalletTransaction_data)
admin.site.register(UserCredit, usercredit_data)
admin.site.register(BankDetails, bankdetails_data)


class orderItemInline(admin.TabularInline):
    model = Order_Request

@admin.register(Order_Details)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['Order_ID']
    inlines = [orderItemInline]

    # def save_model(self, request, obj, form, change):
    #     if obj.Status == "completed":
    #         obj.Completion_Date = obj.Completion_Date + datetime.timedelta(days=7)
    #     obj.save()