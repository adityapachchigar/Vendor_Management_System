from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('create',views.CreateVendor),
    path('api/vendors/', views.VendorListView.as_view()),
    path('api/vendors/<str:pk>/', views.VendorRetrieveView.as_view()),
    # path('list',views.ListVendor),
    # path('retrieve',views.RetrieveVendor),
    # path('update',views.UpdateVendor),
    # path('delete',views.DeleteVendor),
]
