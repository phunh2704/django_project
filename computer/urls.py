from django.urls import path, include
from computer import views


urlpatterns = [    
    path('computer/', views.index, name='index'),
    path('computer/manage/', views.computer_manage, name='computer_list'),       
    path('computer/update/<pcname>/', views.computer_update, name='computer_update'),
    path('computer/delete/<pcname>/', views.computer_delete, name='computer_delete'),
    path('computer/<pcname>/', views.computer_view, name='computer_view'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.SiteLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]
