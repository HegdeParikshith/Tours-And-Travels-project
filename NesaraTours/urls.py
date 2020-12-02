from . import views
from django.contrib.auth import views as auth_views 
from django.urls import path

urlpatterns = [
    path('',views.Home,name='Home'),
    path('packages/', views.Packages, name='packages'),
    path('viewPackage/<str:pk>/',views.ViewPackage,name ='ViewPackage'),
    path('customer/',views.Cust,name='customer'),
    path('login/',views.loginPage,name="login"),
    path('employee/',views.EMp, name='employee'),
    path('emp/<str:Pk>/',views.emp, name='emp'),
    path('branch/',views.branch,name='branch'),
    path('BRANCH/<str:pk>/',views.BRANCH,name='BRANCH'),
    path('tours/',views.Tours,name='Tours'),
    path('logout/', views.logoutUser, name="logout"),
   
    path('reportView/', views.ViewPDF.as_view(), name="pdf_view"),
    path('reportDownload/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('report/',views.Report,name='Report'),
    path('tourdetails/<str:pk>/',views.TourDetails,name='tourdetails'),

    # path('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name="password_reset_done"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),


   
]
