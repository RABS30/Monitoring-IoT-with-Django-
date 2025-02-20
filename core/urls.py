from django.contrib import admin
from django.urls import path, include, re_path

from apiData.views import sensorViewSet
from rest_framework.routers import DefaultRouter

from allauth.account.views import signup, login, logout,password_set, password_change, password_reset, password_reset_done, email_verification_sent, confirm_email, email

router = DefaultRouter()
router.register(r'', sensorViewSet, basename='sensor')


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',            include('dashboard.urls', namespace='dashboard')),
    path('accounts/signup/',  signup, name="account_signup"),
    path('accounts/login/' ,  login,  name="account_login"),
    path('accounts/logout/',  logout, name="account_logout"),
    
    path('accounts/password/set/',    password_set,        name="account_set_password"),
    path('accounts/password/change/', password_change,     name="account_change_password"),
    path('accounts/password/reset/',  password_reset,      name="account_reset_password"),
    path('accounts/reset/done/',      password_reset_done, name="account_reset_password_done"),
    
    path('accounts/email/', email, name="account_email"),
    path('accounts/confirm-email/', email_verification_sent, name="account_email_verification_sent"),
    re_path(r'^accounts/confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name="account_confirm_email"), 
    
    path('api-auth/',   include('rest_framework.urls', namespace='rest_framwork')),
    path('bot/',        include('apiData.urls')),
    path('profile/',    include('profileUser.urls' , namespace='profile')),
    path('sensor/',     include(router.urls)),
]