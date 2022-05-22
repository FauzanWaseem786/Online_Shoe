from . import views
from django.urls import path
app_name='website_model'
urlpatterns=[
path('', views.index, name='index'),#Home page
path('otp/',views.otp,name='otp'),#otp page
path('Membership/',views.Membership,name='Membership'),#registration page
path('Variety/',views.Variety,name='Variety'),
path('brands/',views.brands,name='brands'),
path('location/',views.location,name='location'),
path('membership/',views.Premium,name='Premium'),
path('shoes/',views.shoes,name='shoes'),
path('sandals/',views.sandals,name='sandals'),
path('boots/',views.boots,name='boots'),
path('slippers/',views.slippers,name='slippers'),
path('login/',views.login,name='login'),
path('ilogout/',views.ilogout,name='ilogout'),
path('order/',views.OrDer,name='OrDer'),
path('change/',views.change,name='change'),
path('broadcast_sms/',views.broadcast_sms,name='broadcast_sms'),
path('reg/',views.reg,name='reg'),
path('user/',views.usraccnt,name='usraccnt'),
path('members/',views.allusr,name='allusr'),
path('create_group/',views.crt_grp,name='crt_grp'),
path('groups/',views.grps,name='grps'),
path('groups/<u_name>/',views.grps,name='grps'),
path('pass_change_otp/',views.pass_change_otp,name='pass_change_otp'),
path('dele_accnt/',views.dele_accnt,name='dele_accnt'),
path('edt/',views.edt,name='edt'),
path('edt/<n>/',views.edt,name='edt'),
]
