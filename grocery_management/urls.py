from django.urls import path, include

from grocery_management import views
# from . import views

urlpatterns = [
    path('create/', views.product_create, name='product_create'),
    path('', views.index, name='index'),
    path('manage/', views.product_list, name='product_list'),
    path('update/<int:product_id>/', views.product_update, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete, name='product_delete'),
    path('sell/<int:product_id>/', views.product_sell, name='product_sell'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.SiteLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]
