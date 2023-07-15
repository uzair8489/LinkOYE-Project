from email import header, message
from django.core.mail import EmailMessage
from multiprocessing import context
from urllib import response
from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
from .models import *
from .middlewares import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render
from decimal import Decimal
import random
from random import randint
import string
import requests
import datetime
from tablib import Dataset

# Create your views here.

def index(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'index.html', context)

@login_required
def dashboard(request):
    data1 = []
    ids = list(request.session.get('cart').keys())
    sites = Sites.objects.filter(id__in = ids)
    top_selling_sites = Sites.objects.filter(Selling_Category__Category_Name = 'Top Selling')
    for key, val in request.session.get('cart').items():
        data1.append(val)
    data = Sites.objects.all()
    context={
        'sites': sites,
        'title': data1,
        'top_selling_sites': top_selling_sites,
    }
    return render(request, 'dashboard.html', context)

# def services(request):
#     services = Services.objects.all()
#     context = {
#         'all_services' : services,
#     }
#     return render(request, 'services.html', context)

def guest_posting(request):
    if request.method == 'POST':
        c_name = request.POST['name']
        c_email = request.POST['email']
        subject = request.POST['subject']
        c_message = request.POST['message']
        try:
            message = '{} has sent a message\n'.format(c_email)
            message += 'Name: {}\n'.format(c_name)
            message += 'Message:\n{}'.format(c_message)

            # Send the email to the customer
            send_mail(
                subject,
                message,
                'info@linkoye.co',
                ['info@linkoye.co'],
                fail_silently=False
            )
            messages.info(request,'Thank you for contacting us. We have received your message and will get back to you shortly')
            return redirect('guest_posting')
        except Exception as e:
            messages.info(request, e)
            return redirect('guest_posting')
    return render(request, 'guest_posting.html')

# def services_details(request, pk):
#     service_detail = Services.objects.get(id = pk)
#     context = {
#         'service_detail' : service_detail,
#     }
#     return render(request, 'services_details.html', context)

# Login Module 
def login(request):
    if request.user.is_authenticated:
            return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            request.session['cart'] = {}
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def blogs(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs.html', context)

def blogs_details(request, pk):
    blog_detail = Blogs.objects.filter(id = pk)
    context = {
        'blog_detail' : blog_detail,
    }
    return render(request, 'blogs_details.html', context)

@login_required
def myorders(request):
    ids = list(request.session.get('cart').keys())
    sites = Sites.objects.filter(id__in = ids)
    # print(status.Customer)
    orders = Order_Request.objects.filter(Customer = request.user)
    context = {
        'orders': orders,
        'sites' : sites,
    }
    return render(request, 'myorders.html', context)

@login_required
def quickpurchase(request):
    data1 = []
    # request.session['cart'] = {}
    # request.session.get('cart').clear()
    ids = list(request.session.get('cart').keys())
    # print(request.session.get('cart').keys())
    sites = Sites.objects.filter(id__in = ids)
    for key, val in request.session.get('cart').items():
        data1.append(val)
    # print(data1)
        # for i in val:
        # print("--------------------")
    # print(data1)
    # if request.method=='POST':
    #     siteid = request.POST['siteid']
    #     cart = request.session.get('cart')
    #     if cart:
    #         cart[siteid] = 1
    #     else:
    #         cart = {}
    #         cart[siteid] = 1
    #     request.session['cart'] = cart
    #     return redirect('quickpurchase')

    data = Sites.objects.all()
    context={
        'sites_data': data,
        'sites': sites,
        'title': data1
    }
    # print(request.session.get('cart'))    
    return render(request, 'quickpurchase.html', context)

@login_required_pk
def site_details(request, url):
    site_detail = Sites.objects.filter(URL = url)
    context = {
        'site_detail' : site_detail,
    }
    return render(request, 'site_details.html', context)

@login_required
def wallet(request):
    ids = list(request.session.get('cart').keys())
    sites = Sites.objects.filter(id__in = ids)
    usr = UserCredit.objects.get(user = request.user)
    context = {
        'credit' : usr,
        'sites': sites,
    }
    return render(request, 'wallet.html',context)

@login_required
def wallet_transactions(request):
    transactions = WalletTransaction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'wallet_transactions.html', {'transactions': transactions})

#for uploading the webistes data
def upload(request):
    if request.user.is_superuser:
        data = Sites.objects.all()
        # data = Person.objects.all()
        #print(data)
        if request.method == 'POST':
            # Person_resource = PersonResource()
            dataset = Dataset()
            sites_data = request.FILES['myfile']

            # if not new_person.name.endswith('xlsx'):
            #     messages.info(request, 'wrong format')
            #     return render(request, 'upload.html',{'messages':data})
            imported_data = dataset.load(sites_data.read(),format='xlsx')
            for data in imported_data:
                # print(data)
                value = Sites(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                    data[9],
                    data[10],
                    data[11],
                    data[12],
                    data[13],
                    data[14],
                    )
                value.save()
            messages.info(request,'File Uploaded Successfully.')
            # print('data Saved')
            # messages.success(request, 'Your File Upload')
        # return render(request, 'enroll/upload.html',{'messages':data})
        return render(request, 'upload.html')
    else:
        return render(request, 'error-404.html')

#user profile
@login_required
def userprofile(request):
    usr = User_Profile.objects.filter(user = request.user)
    context ={
        'user_d': usr
    }
    return render(request, 'userprofile.html', context)

#buy post module
@login_required_pk
def buypost(request, url):
    ids = list(request.session.get('cart').keys())
    sites = Sites.objects.filter(id__in = ids)
    site_data = Sites.objects.filter(URL = url)
    one = 1
    cart = request.session['cart']
    # site_data ={}
    # request.session.get('cart').clear()
    if request.method == 'POST':
        siteid = request.POST['sid']
        title = request.POST.get('title')
        keywords = request.POST.getlist('keyword')
        linktype = request.POST.getlist('link-type')
        URL = request.POST.get('URL')
        price = request.POST.get('price')
        urls = request.POST.getlist('url')
        limit_time = request.POST.get('limit_time')
        odetails = request.POST.get('odetails')
        imgurl = request.POST.get('imgurl')
        avoidingterms = request.POST.get('avoidingterms')
        infosource = request.POST.get('infosource')
        cart = request.session.get('cart')
        if cart:
            cart[siteid] = one,URL,title,limit_time,keywords,urls,linktype,odetails,imgurl,avoidingterms,infosource,price
        else:
            cart = {}
            cart[siteid] = one,URL,title,limit_time,keywords,urls,linktype,odetails,imgurl,avoidingterms,infosource,price
        request.session['cart']= cart
        print(request.session.get('cart'))
        return redirect('buypost', url)
    context={
        'site_data' : site_data,
        'sites': sites,
    }
    # print(request.session['cart'])
    return render(request, 'buypost.html', context)

#cart module
@login_required
def cart(request):
    # print(request.session.get('cart'))
    site_data =''
    data1 = []
    ids = list(request.session.get('cart').keys())
    sites = Sites.objects.filter(id__in = ids)
    for key, val in request.session.get('cart').items():
        data1.append(val)
    # for items in data1:
    #     print(items[7])
    if request.method == 'POST':
        siteid = request.POST['siteid']
        remove = request.POST['remove']
        site_data = Sites.objects.filter(id = siteid)
        cart = request.session.get('cart')
        if cart:
            if remove:
                cart.pop(siteid)
        request.session['cart'] = cart
        return redirect('cart')
    context ={
        'sites': sites,
        'site_data': site_data,
        'title': zip(data1,sites)
    }
    return render(request, 'cart.html',context)

#checkout module
@denied_access_checkout
def checkout(request):
    # print(request.user.id)
    site_data =''
    data1 = []
    bank_details = BankDetails.objects.get(id=1)
    file_path = bank_details.File.path
    with open(file_path, 'rb') as f:
        file_data = f.read()
    ids = list(request.session.get('cart').keys())
    sites = Sites.objects.filter(id__in = ids)
    usr = UserCredit.objects.get(user = request.user)
    for key, val in request.session.get('cart').items():
        data1.append(val)
    if request.method == 'POST':
        total_ = request.POST['total']
        payment_method = request.POST.get("payment_way")
        now=datetime.datetime.now()
        # print(max_val)
        if payment_method == "wallet credit":
            if usr.credit < Decimal(total_):
                messages.info(request,'Insufficient Credit, please add credit or choose another payment method.')
                return redirect('checkout')
            else:
                Order_Details.objects.create(Order_Total = request.POST['total'], Customer = request.user)
                max_val = Order_Details.objects.latest('Order_ID')
                max_val.Payment_Method = 'wallet credit'
                max_val.Paid = 'paid'
                max_val.save()
                usr.credit -= Decimal(total_)
                usr.save()
                for items in data1:
                    Order_Request.objects.create(Order_ID = max_val,
                    Customer = request.user,
                    URL = items[1],
                    Title = items[2],
                    Order_Date = now.strftime("%Y-%m-%d"),
                    Order_Deadline = items[3],
                    keywords = items[4],
                    urls = items[5],
                    link_Type = items[6],
                    details = items[7],
                    image_url = items[8],
                    terms_to_avoid = items[9],
                    info_source = items[10],
                    Price = items[11],
                    )
                    try:
                        subject = 'Order Confirmation: Order #{}'.format(max_val.Order_ID)
                        message = 'Dear {},\n\nYour order has been placed successfully.\n\n'.format(request.user.username)
                        message += 'Order Details:\n'
                        message += 'Order ID: {}\n'.format(max_val.Order_ID)
                        message += 'Order Total: ${}\n'.format(max_val.Order_Total)
                        message += 'Payment Method: {}\n'.format(max_val.Payment_Method)
                        message += 'Paid: {}\n\n'.format(max_val.Paid)
                        message += 'Thank you for choosing us.\n\nBest Regards,\nLinkOYE'

                        # Send the email to the customer
                        send_mail(
                            subject,
                            message,
                            'info@linkoye.co',
                            [request.user.email],
                            fail_silently=False
                        )
                    except Exception as e:
                        print(e)
        else:
            # max_val.Customer = request.user.id
            Order_Details.objects.create(Order_Total = request.POST['total'], Customer = request.user)
            max_val = Order_Details.objects.latest('Order_ID')
            max_val.Payment_Method = 'bank transfer'
            max_val.Paid = 'not paid'
            max_val.save()
            for items in data1:
                Order_Request.objects.create(Order_ID = max_val,
                Customer = request.user,
                URL = items[1],
                Title = items[2],
                Order_Date = now.strftime("%Y-%m-%d"),
                Order_Deadline = items[3],
                keywords = items[4],
                urls = items[5],
                link_Type = items[6],
                details = items[7],
                image_url = items[8],
                terms_to_avoid = items[9],
                info_source = items[10],
                Price = items[11],
                )
                try:
                    subject = 'Order Confirmation: Order #{}'.format(max_val.Order_ID)
                    message = 'Dear {},\n\nYour order has been placed successfully.\n\nA file containing account details has also been attached with this email.\n\nPlease transfer the amount to the following bank account for completing the order.\n\nBank Name: {}\nAccount Number: {}\nIBAN Code: {}\n\n'.format(request.user.username, bank_details.bank_name, bank_details.account_number, bank_details.IBAN)
                    message += 'Order Details:\n'
                    message += 'Order ID: {}\n'.format(max_val.Order_ID)
                    message += 'Order Total: ${}\n'.format(max_val.Order_Total)
                    message += 'Payment Method: {}\n'.format(max_val.Payment_Method)
                    message += 'Paid: {}\n\n'.format(max_val.Paid)
                    message += 'Thank you for choosing us.\n\nBest Regards,\nLinkOYE'

                    # Send the email to the customer
                    email = EmailMessage(
                        subject=subject,
                        body=message,
                        from_email='info@linkoye.co',
                        to=[request.user.email],
                    )
                    email.attach('bank_details.pdf', file_data, 'application/pdf')
                    email.send()
                except Exception as e:
                    print(e)
            
                # send_mail(
                #     'Order Confirmation : Order #{}'.format(max_val),
                #     f'Dear customer,\n\nYour order has been placed successfully. Please transfer the amount to the following bank account for completing the order.\n\nBank Name: {bank_details.bank_name}\nAccount Number: {bank_details.account_number}\nIBAN Code: {bank_details.IBAN}\n\nRegards,\nLinkOYE',
                #     'info@linkoye.co',
                #     ['uzair8489@gmail.com'],
                #     fail_silently=False,
                # )

        vat = request.POST['vat']
        if not vat:
                    vat = '0.00'
        bd = Billing_Details(
        Order_ID = max_val,
        Country = request.POST['country'],
        First_Name = request.POST['first_name'],
        Last_Name = request.POST['last_name'],
        Company_Name = request.POST['company'],
        VAT = vat,
        Address = request.POST['address'],
        City = request.POST['city'],
        State = request.POST['state'],
        Zip_Code = request.POST['zip'],
        Email = request.POST['email'],
        Phone = request.POST['phone'],
        Order_Notes = request.POST['notes'],
        )
        bd.save()
        request.session['cart'] = {}
        return redirect('/ordersuccess')
    context ={
        'user_balance' : usr,
        'sites': sites,
        'site_data': site_data,
        'title': zip(data1,sites)
    }   
    # print(usr.credit)
    return render(request, 'checkout-1.html', context) 


def ordersuccess(request):
    return render(request, 'ordersuccess.html')

#wallet top up module
def top_up_wallet(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        order_id = str(randint(100000, 999999))
        bank_details = BankDetails.objects.first()
        IBAN = bank_details.IBAN


        WalletTransaction.objects.create(
            order_id=order_id,
            amount=amount,
            IBAN=IBAN,
            user=request.user
        )
        # Redirect to the success page with the necessary parameters
        return redirect('top_up_success', order_id=order_id, amount=amount, IBAN=IBAN)

    return render(request, 'topupform.html')

def top_up_success(request, order_id, amount, IBAN):
    return render(request, 'top_up_success.html', {'order_id': order_id, 'amount': amount, 'IBAN': IBAN})

def about_us(request):
    return render(request, 'about_us.html')

from django.core.mail import send_mail


#sign up module
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        country = request.POST['country']
        city = request.POST['city']
        postal_code = request.POST['postal_code']
        address = request.POST['address']
        company = request.POST['company']
        VAT = request.POST['VAT']
        website = request.POST['website']

        if len(password1) < 8:
            messages.info(request,'Your password must be 8 character long.')
            return redirect('signup')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Taken')
            elif User_Profile.objects.filter(contact=phone).exists():
                messages.info(request,'Phone number linked with another account')
            else:
                user = User.objects.create_user(first_name=first_name, last_name = last_name, username = username, email = email, password = password1)
                user.save()

                if not VAT:
                    VAT = '0.00'

                user_d = User_Profile(user = user, contact = phone, country = country, city = city, postal_code = postal_code, address = address, company = company, VAT = VAT, website = website)
                user_d.save()

                uc = UserCredit(user = user, credit = '0.00')
                uc.save()

                try:
                    subject = 'Account created Successfully'
                    message = 'Dear {},\n\nYour account on LinkOYE has been created successfully.'.format(first_name)
                    message += ' You can login now using your credentials.\n'
                    message += 'Thank you for choosing us.\n\nBest Regards,\nLinkOYE'

                    # Send the email to the customer
                    send_mail(
                        subject,
                        message,
                        'info@linkoye.co',
                        [email],
                        fail_silently=False
                    )
                except Exception as e:
                    pass

                messages.info(request,'Account created successfully. You can login in now.')
                return redirect('login')


        else:
            messages.info(request,'Password does not match')
            # print('password not matching...')
        return redirect('signup')

    else:
        return render(request, 'register.html')


#logout module
def logout(request):
    request.session['cart'] = {}
    auth.logout(request)
    return redirect('/')