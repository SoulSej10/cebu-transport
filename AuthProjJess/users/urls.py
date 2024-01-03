from django.urls import path
from django.contrib import admin
from django.conf import settings
from.import views
from django.conf.urls.static import static

urlpatterns = [
   path('', views.home, name='home'),
   path('billing/', views.billing, name = 'billing'),
   path('about/', views.about, name = 'about'),
   path('explore/', views.explore, name = 'explore'),
   path('Log/', views.Log, name = 'Log'),
   path('memereq/', views.memereq, name = 'memereq'),
   path('Register/', views.Register, name = 'Register'),
   path('users/', views.all_Request, name = 'Request_list'),
   path('login_reg/',views.login_reg, name = 'login_reg'),
   path('log_out/',views.log_out, name = 'log_out'),
   path('register/',views.registerUser, name = 'register'),

   path('bus/', views.bus_ticket, name='bus_ticket'),
   path('bus_ticket_signed_up/', views.bus_ticket_signed_up, name='bus_ticket_signed_up'),

   path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)