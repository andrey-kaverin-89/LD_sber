from django.urls import path
from Sber_mail import views

urlpatterns = [
    path('update/', views.update),
    path('mails/<int:priority>/', views.mail_list_priority),
    path('mails/', views.mail_list),
    path('mail/<int:pk>/<int:priority>/', views.mail_detail),
    path('unsee/<int:pk>/', views.mail_unsee),
    # path('voice/<int:pk>/'),
    # # path('movepriority/<int:pk>/'),
    path('forwardlist/<int:pk>/', views.forwardlist), # список кому отправлять - только люди
    # path('send/'), # POST 1) to_addrs 2) subject 3) text - сама отправка
]