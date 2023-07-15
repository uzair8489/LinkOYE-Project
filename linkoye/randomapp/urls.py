from re import template
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs_details/<str:pk>', views.blogs_details, name='blogs_details'),
    path('myorders', views.myorders, name='myorders'),
    path('quickpurchase', views.quickpurchase, name='quickpurchase'),
    path('site_details/<str:url>', views.site_details, name='site_details'),
    path('wallet', views.wallet, name='wallet'),
    path('wallet_transactions', views.wallet_transactions, name='wallet_transactions'),
    path('upload', views.upload, name='upload'),
    path('buypost/<str:url>', views.buypost, name='buypost'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('about_us', views.about_us, name='about_us'),
    path('guest_posting', views.guest_posting, name='guest_posting'),
    # path('services', views.services, name='services'),
    # path('services_details/<str:pk>', views.services_details, name='services_details'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('top_up_wallet', views.top_up_wallet, name='top_up'),
    path('top_up-success/<str:order_id>/<str:amount>/<str:IBAN>/', views.top_up_success, name='top_up_success'),
    path('ordersuccess', views.ordersuccess, name='ordersuccess'),
    path('change_password', auth_views.PasswordChangeView.as_view(template_name = 'change_password.html'), name='change_password'),  
    path('change_password_done', auth_views.PasswordResetDoneView.as_view(template_name = 'change_password_done.html'), name='password_change_done'),  
    path('reset_password', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name = "reset_password_sent.html"), name ="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "reset_password_form.html"), name ="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name = "reset_password_done.html"), name ="password_reset_complete"),
]