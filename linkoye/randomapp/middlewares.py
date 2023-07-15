from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login_required(get_response):
   

    def middleware(request):
        if not request.user.is_authenticated:
            messages.info(request,'You must login first')
            return redirect('login')
        
        # print(request.user)
        response = get_response(request)
        return response

    return middleware

def login_required_pk(get_response):
   

    def middleware(request, url):
        if not request.user.is_authenticated:
            messages.info(request,'You Must Login First')
            return redirect('login')
        
        # print(request.user)
        response = get_response(request, url)
        return response

    return middleware

def denied_access(get_response):
   

    def middleware(request):
        if not request.user.is_authenticated:
            return redirect('/')
            
        if request.user.is_authenticated:
            return redirect('/')
        
        # print(request.user)
        response = get_response(request)
        return response

    return middleware

def denied_access_checkout(get_response):
   

    def middleware(request):
        if not request.user.is_authenticated:
            messages.info(request,'You must login first')
            return redirect('login')
        if request.session['cart'] == {}:
            return redirect('/cart')
        response = get_response(request)
        return response

    return middleware










